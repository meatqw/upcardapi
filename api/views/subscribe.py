from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.http import Http404
from api.models import *
from api.serializers import *
from rest_framework import status
import requests
from datetime import datetime

def send_message_email_subscribe(email):
    
    headers = {
        'authorization': '7X5l68iaYji64yMjDKE7p1ksROdFkJFhwzts'
    }

    data = {
        'subject': 'UpCard Подписка',
        'html': f'<html><head></head><body><p>Вы оформили базовую подписку.</p></body></html>',
        'from': 'admin@upcard.online',
        'to': f'{email}'
    }
    
    request = requests.post('https://api.smtp.bz/v1/smtp/send', headers=headers, data=data)
    return request.json()['result']


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
                
                send_message_email_subscribe(account.email)
                
                
                
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)
        
    serializer_class = UserSubscribeSerializer