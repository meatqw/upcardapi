from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.http import Http404
from api.models import *
from api.serializers import *
from rest_framework import status


class CompanyAPIPost(APIView):
    """Добавить информацию о компании по токену пользвоателя"""

    def post(self, request, *args, **kwargs):
        
        token = self.request.GET.get('token')
        account = Account.objects.filter(token=token).first()
        data = request.data
        
        if account:
            company_serializer = CompanyInfoPOSTSerializer(data=data)
            if company_serializer.is_valid():
                company = company_serializer.save()
                response_serializer = CompanyInfoSerializer(company)
                
                return Response(response_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No account found'}, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = CompanyInfoSerializer


class CompanyAPIView(viewsets.ReadOnlyModelViewSet):
    """Получить информацию по id и токену пользвоателя"""

    def get_queryset(self):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                company = CompanyInfo.objects.filter(id=self.kwargs['id']).all()

                return company
            else:
                raise Http404("No Data")
        else:
            raise ValidationError("No Token")

    serializer_class = CompanyInfoSerializer


class CompanyAPIUpdate(APIView):
    """
    Обновить информациб о компании
    """
    def patch(self, request, *args, **kwargs):
        if "token" in self.request.GET:
            token = self.request.GET['token']
            account = Account.objects.filter(token=token).first()
            if account:
                company = CompanyInfo.objects.filter(id=self.kwargs['id']).first()

                company_serializer = CompanyInfoPOSTSerializer(
                    data=request.data, instance=company, partial=True)
                company_serializer.is_valid(raise_exception=True)
                company = company_serializer.save()
                
                respone_serialezer = CompanyInfoSerializer(company)
                
                return Response(respone_serialezer.data)
            else:
                return Response({'error': "No data"})
        else:
            return Response({'error': "No token"})

        

    serializer_class = CompanyInfoSerializer
