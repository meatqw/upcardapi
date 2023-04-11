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


class PortfolioAPIPost(APIView):
    """Добавить елементы портфолио"""

    def post(self, request, *args, **kwargs):

        # Get the associated Account object
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        
        if account:
            # приводим дату в нужынй вид
            data = request.data.copy()
            for key, value in data.items():
                if key == 'date':
                    data[key] = datetime.strptime(data[key], "%Y-%m-%d")
            
            data['id_account'] = account.id
            
            portfolio = PortfolioPOSTSerializer(data=data)
            if portfolio.is_valid():
                portfolio.save()
                
                response_serializer = PortfolioSerializer(portfolio)
                
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(portfolio.errors, status=status.HTTP_400_BAD_REQUEST)

            
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = PortfolioSerializer


class PortfolioAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить портфолио по id и токену"""

    def get_queryset(self):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                portfolio = Portfolio.objects.filter(id=self.kwargs['id']).all()

                return portfolio
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No Token")

    serializer_class = PortfolioSerializer
    
    
class PortfolioByCardAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить портфолио по id card и токену"""

    def get_queryset(self):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            
            if account:
                portfolio = Portfolio.objects.filter(id_card=self.kwargs['id_card']).all()

                return portfolio
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No Token")

    serializer_class = PortfolioSerializer
    

class PortfolioByCardNoTokenAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить портфолио по id card"""

    def get_queryset(self):
        if "id_card" in self.request.GET:
            id_card = self.request.GET['id_card']
            portfolio = Portfolio.objects.filter(id_card=id_card).all()
            
            if portfolio:
                
                return portfolio
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No Id Card")

    serializer_class = PortfolioSerializer


class PortfolioAPIUpdate(APIView):
    """
    Обновить элемент портфолио
    """
    def patch(self, request, *args, **kwargs):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            
            if account:
                portfolio = Portfolio.objects.filter(id=self.kwargs['id']).first()
                
                # приводим дату в нужынй вид
                data = request.data.copy()
                for key, value in data.items():
                    if key == 'date':
                        data[key] = datetime.strptime(data[key], "%Y-%m-%d")
                
                serializer = PortfolioPOSTSerializer(
                    data=data, instance=portfolio, partial=True)
                
                serializer.is_valid(raise_exception=True)
                portfolio_serializer = serializer.save()
                
                print('request.data:', request.data)
                print('portfolio:', portfolio.date)
                
                response_serializer = PortfolioSerializer(portfolio_serializer)
                
                return Response(response_serializer.data)
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

        

    serializer_class = PortfolioSerializer
    
    
class PortfolioAPIDelete(APIView):
    """
    Удалить элемент порфолио
    """
    def delete(self, request, id):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()

            if account:
                portfolio = Portfolio.objects.filter(id=id).first()
                if portfolio:
                    portfolio.delete()
                    return Response({'success': "Portfolio deleted successfully"})
                else:
                    return Response({'error': "Portfolio not found"})
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})
