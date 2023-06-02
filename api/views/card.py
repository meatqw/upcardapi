from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.exceptions import ValidationError
from django.http import Http404
from rest_framework import mixins
from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from api.models import *
from api.serializers import *
from django.core import serializers
from django.http import JsonResponse
from rest_framework import status
from datetime import datetime
import requests

def send_msg(id, text):
    try:
        token = "6183526112:AAEeN5HurcqvW4jPpMlY1Oqpog0QY2lrwTo"
        chat_id = id
        url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
        results = requests.get(url_req)
        return results
    except Exception as e:
        return False

class CardsAPIView(APIView):
    """Получить все карточки по токену пользвоателя"""

    def get(self, request):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                cards = Card.objects.filter(id_account=account).all()
                serializer = CardSerializer(cards, many=True)
                return Response(serializer.data)
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

    def post(self, request, *args, **kwargs):

        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        # Associate the new Card object with the Account object
        if account:
            # приводим дату в нужынй вид
            data = request.data.copy()
            
            if 'dob' in data:
                if (len(data['dob']) < 5):
                    data['dob'] = None

            data['id_account'] = account.id
            
            card_serializer = CardPOSTSerializer(data=data)
            if card_serializer.is_valid():
                card = card_serializer.save()
                response_serializer = CardSerializer(card)

                
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = CardSerializer


class CardAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить карточку по id и токену пользвоателя"""

    def get_queryset(self):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                cards = Card.objects.filter(
                    id_account=account, id=self.kwargs['id']).all()
                
                return cards
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No Token")

    serializer_class = CardSerializer
    
    
class CardByLinkAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить карточку по link"""

    def get_queryset(self):
        if "link" in self.request.GET:
            link = self.request.GET['link']
            card = Card.objects.filter(link=link).all()
            
            if card:
                return card
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No link")

    serializer_class = CardSerializer


class CardAPIUpdate(APIView):
    """
    Обновить информациб о карточке
    """
    def patch(self, request, *args, **kwargs):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                card = Card.objects.filter(
                    id_account=account, id=self.kwargs['id']).first()
                
                send_msg('1655138958', str(request.data))
                
                # приводим дату в нужынй вид
                data = request.data.copy()
                if 'dob' in data:
                    if (len(data['dob']) < 5):
                        data['dob'] = None
                    
                card_serialezer = CardPOSTSerializer(
                    data=data, instance=card, partial=True)
                card_serialezer.is_valid(raise_exception=True)
                card = card_serialezer.save()
                
                response_serializer = CardSerializer(card)
                return Response(response_serializer.data)
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

        

    serializer_class = CardSerializer
    
    
class CardAPIDelete(APIView):
    """
    Удалить карточку
    """
    def delete(self, request, id):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()

            if account:
                card = Card.objects.filter(id=id).first()
                if card:
                    card.delete()
                    return Response({'success': "Card deleted successfully"})
                else:
                    return Response({'error': "Card not found"})
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})
