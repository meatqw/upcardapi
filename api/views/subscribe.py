from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *
from rest_framework import status
from services.send_message_service import SendMsg


class SubscribeAPIPost(APIView):
    """Офрмить подписку"""

    def post(self, request, *args, **kwargs):
        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()

        user_subscribe = UserSubscribeSerializer(data=request.data)

        if account:
            if user_subscribe.is_valid():

                user_subscribe = user_subscribe.save()
                UserSubscribeSerializer(user_subscribe)

                SendMsg.send_message_email_subscribe(account.email)

                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = UserSubscribeSerializer
