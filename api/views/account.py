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


class AccountAPIView(APIView):
    """Получить все карточки по токену пользвоателя"""

    def get(self, request):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                serializer = AccountSerializer(account)
                return Response(serializer.data)
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

    def patch(self, request, *args, **kwargs):

        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        if account:
            data = request.data.copy()
            if (data['id_subscription'] == 'null'): data['id_subscription'] = None
                
            
            account_serilizer = AccountSerializer(data=data, instance=account, partial=True)
            if account_serilizer.is_valid(raise_exception=True):
                account_ = account_serilizer.save()

                response_serializer = AccountSerializer(account_)

                return Response({'data': response_serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(account_serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

