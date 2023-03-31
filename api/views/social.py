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


class SocialAPIPost(APIView):
    """Добавить ифно о социалках"""

    def post(self, request, *args, **kwargs):

        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        data = request.data
        
        if account:
            data['id_account'] = account.id
            social = SocialSerializer(data=data)
            if social.is_valid():
                social.save()
            else:
                return Response(social.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'id': social.instance.id}, status=status.HTTP_201_CREATED)
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
                social = Portfolio.objects.filter(id=self.kwargs['id']).first()

                serializer = SocialSerializer(
                    data=request.data, instance=social, partial=True)
                
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

        return Response(serializer.data)

    serializer_class = SocialSerializer