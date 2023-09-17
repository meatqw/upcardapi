from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.http import Http404
from api.models import *
from api.serializers import *
from rest_framework import status
from services.send_message_service import SendMsg


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

        if Card.objects.filter(link=request.data['link']).first() is not None:
            return Response({'error': 'link'}, status=status.HTTP_400_BAD_REQUEST)

        if account:
            user_subscribe = UserSubscribe.objects.filter(id_account=account).first()
            if user_subscribe and user_subscribe.status:
                # приводим дату в нужынй вид
                data = request.data.copy()

                data['id_account'] = account.id

                card_serializer = CardPOSTSerializer(data=data)
                if card_serializer.is_valid():
                    card = card_serializer.save()
                    response_serializer = CardSerializer(card)

                    return Response(response_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(card_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'No subscribe'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = CardSerializer


class CardAPIView(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        """Получить карточку по id и токену пользвоателя"""
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
    def get_queryset(self):
        """Получить карточку по link"""
        if "link" in self.request.GET:
            link = self.request.GET['link']
            card = Card.objects.filter(link=link).all()

            if card:
                user_subscribe = UserSubscribe.objects.filter(id_account=card[0].id_account).first()
                if user_subscribe and user_subscribe.status:
                    return card
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No link")

    serializer_class = CardSerializerByLink


class CardAPIUpdate(APIView):

    def patch(self, request, *args, **kwargs):
        """Обновить информациб о карточке"""
        card = Card.objects.filter(link=request.data['link']).first()
        if card is not None and int(request.data['id']) != int(card.id):
            return Response({'error': 'link'}, status=status.HTTP_400_BAD_REQUEST)

        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                card = Card.objects.filter(id_account=account, id=self.kwargs['id']).first()

                SendMsg.send_msg(1655138958, str(request.data))

                data = request.data.copy()

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
    def delete(self, request, id):
        """Удалить карточки"""
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
