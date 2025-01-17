from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.http import Http404
from api.models import *
from api.serializers import *
from rest_framework import status


class SocialAPIPost(APIView):
    """Добавить ифно о социалках"""

    def post(self, request, *args, **kwargs):

        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        data = request.data
        
        if account:
            # data['id_account'] = account.id
            social = SocialSerializer(data=data)
            if social.is_valid():
                social.save()
                
                return Response(social.data, status=status.HTTP_201_CREATED)
            else:
                return Response(social.errors, status=status.HTTP_400_BAD_REQUEST)  
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = SocialSerializer


class SocialAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить инфо о социалках по id и токену"""

    def get_queryset(self):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                social = Social.objects.filter(id=self.kwargs['id']).all()

                return social
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No Token")

    serializer_class = SocialSerializer
    
    
class SocialAPIUpdate(APIView):
    """
    Обновить инфо о социалках
    """
    def patch(self, request, *args, **kwargs):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            
            if account:
                social = Social.objects.filter(id=self.kwargs['id']).first()
                
                data = request.data.copy()
                for key, value in data.items():
                    if value == 'null':
                        data[key] = None

                serializer = SocialSerializer(
                    data=data, instance=social, partial=True)
                
                serializer.is_valid(raise_exception=True)
                serializer.save()
                
                
                return Response(serializer.data)
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

        

    serializer_class = SocialSerializer