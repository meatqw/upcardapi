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


class SubscriptionAPIView(APIView):
    """Получить все подписки по токену пользвоателя"""

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

