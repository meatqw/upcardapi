from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import *
from api.serializers import *
from rest_framework import status


class ImageAPIPost(APIView):
    """Добавить изображение"""

    def post(self, request, *args, **kwargs):

        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        data = request.data
        
        if account:
            data['id_account'] = account.id
            image = ImageSerializer(data=data)
            if image.is_valid():
                image.save()
            else:
                return Response(image.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'id': image.instance.id}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = Image