from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *


urlpatterns = [
    
    # cards
    path('card/', CardsAPIView.as_view()),
    path('card/<int:id>/', CardAPIView.as_view({'get': 'list'})),
    path('cardUpdate/<int:id>/', CardAPIUpdate.as_view()),
    path('cardLink/', CardByLinkAPIView.as_view({'get': 'list'})),
    path('cardDelete/<int:id>/', CardAPIDelete.as_view()),
    
    # company
    path('company/', CompanyAPIPost.as_view()),
    path('company/<int:id>/', CompanyAPIView.as_view({'get': 'list'})),
    path('companyUpdate/<int:id>/', CompanyAPIUpdate.as_view()),
    
    # portfolio
    path('portfolio/', PortfolioAPIPost.as_view()),
    path('portfolio/<int:id>/', PortfolioAPIView.as_view({'get': 'list'})),
    path('portfolioByCard/<int:id_card>/', PortfolioByCardAPIView.as_view({'get': 'list'})),
    path('portfolioUpdate/<int:id>/', PortfolioAPIUpdate.as_view()),
    path('portfolioDelete/<int:id>/', PortfolioAPIDelete.as_view()),
    path('portfolioCard/', PortfolioByCardNoTokenAPIView.as_view({'get': 'list'})),
    
    
    # social
    path('social/', SocialAPIPost.as_view()),
    path('social/<int:id>/', SocialAPIView.as_view({'get': 'list'})),
    path('socialUpdate/<int:id>/', SocialAPIUpdate.as_view()),
    
    # token test
    path('tokenCheck/', TokenCheckAPIView.as_view()),
    
    
    # image
    path('image/', ImageAPIPost.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)