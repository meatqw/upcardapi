from django.urls import path, include, re_path
# from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)