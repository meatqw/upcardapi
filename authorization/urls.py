from django.urls import path, include, re_path
# from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
from authorization.views import *

urlpatterns = [
    path('welcome/', welcome, name="welcome"),
    path('login/', login, name="login"),
    path('referral/', referral, name="referral"),
    path('invalid/', invalidToken, name="invalid_token"),
    path('sended/', emailSended, name="email_sended"),
    
    path('token/<str:uidb64>/<str:token>/', auth_token, name='auth_token'),
]