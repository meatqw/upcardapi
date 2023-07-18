from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *
from rest_framework import status


class TokenCheckAPIView(APIView):
    """Проверка токена"""

    def post(self, request, *args, **kwargs):
        token = self.request.data.get('token')
        if not token:
            return Response({'status': False}, status=status.HTTP_400_BAD_REQUEST)
        
        account = Account.objects.filter(token=token, is_active=True).first()
        if account:
            return Response({'status': True}, status=status.HTTP_200_OK)
        else:
            return Response({'status': False}, status=status.HTTP_400_BAD_REQUEST)
