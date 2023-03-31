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
        data = request.data
        # Associate the new Card object with the Account object
        if account:
            data['id_account'] = account.id
            card = CardPOSTSerializer(data=data)
            if card.is_valid():
                card.save()
            else:
                return Response(card.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'id': card.instance.id}, status=status.HTTP_201_CREATED)
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

                serializer = CardSerializer(
                    data=request.data, instance=card, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

        return Response(serializer.data)

    serializer_class = CardSerializer
