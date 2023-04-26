from django.urls import path, include, re_path
# from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
from landing.views import *

urlpatterns = [
    path('', index, name="index"),

]