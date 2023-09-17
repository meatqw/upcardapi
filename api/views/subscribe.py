from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *
from rest_framework import status
from services.send_message_service import SendMsg
from services.tinkoff.tinkoff_service import Tinkoff
import time
from django.utils import timezone


class SubscribeAPI(APIView):
    """Офрмить подписку"""
    def get(self, request):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                subscribe = UserSubscribe.objects.filter(id_account=account).first()
                if subscribe:
                    return Response({
                        'status': subscribe.status,
                        'cardCount': subscribe.card_count,
                        'price': subscribe.price,
                        'expireAt': subscribe.expire_at.strftime("%Y.%m.%d"),
                        'paymentURL': subscribe.payment_id.payment_url}
                        )
                else:
                    return Response({'status': False})

            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

    def post(self, request, *args, **kwargs):
        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        data = request.data.copy()

        if data['price'] < 100:
            SendMsg.send_msg(1655138958, 'PRICE LOW CODE')
            return Response({'status': 'price'})

        if account:
            new_payment = self.create_payment(data, account)
            data['account_id'] = account
            data['payment_id'] = new_payment
            data['expires_at'] = timezone.now() + timezone.timedelta(days=30)
            data['status'] = False

            if UserSubscribeSerializer(data=request.data).is_valid():

                UserSubscribe.objects.update_or_create(
                    id_account=account,
                    defaults={
                        'id_account': account,
                        'status': data['status'],
                        'expire_at': data['expires_at'],
                        'payment_id': data['payment_id'],
                        'card_count': data['card_count'],
                        'price': data['price'],
                        'id_subscription': Subscription.objects.filter(id=data['id_subscription']).first()
                    }
                )

                SendMsg.send_message_email_subscribe(account.email)

                return Response({'status': 'success', 'payment_url': new_payment.payment_url},
                                status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = UserSubscribeSerializer

    @staticmethod
    def create_payment(request_data: dict, account: Account):
        request_data['OrderId'] = str(time.time()).split('.')[0]
        request_data['Amount'] = request_data['price']

        tinkoff = Tinkoff()
        data = tinkoff.init(request_data)


        new_payment = Payment(
            payment_id=data['PaymentId'],
            payment_url=data['PaymentURL'],
            amount=data['Amount'],
            status=data['Status'],
            account_id=account
        )

        new_payment.save()
        return new_payment

