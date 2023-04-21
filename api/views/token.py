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


class TokenCheckAPIView(APIView):
    """Проверка токена"""

    def post(self, request, *args, **kwargs):
        token = self.request.data.get('token')
        if not token:
            return Response({'status': False}, status=status.HTTP_400_BAD_REQUEST)
        
        account = Account.objects.filter(token=token).first()
        if account:
            return Response({'status': True}, status=status.HTTP_200_OK)
        else:
            return Response({'status': False}, status=status.HTTP_400_BAD_REQUEST)
