from django.urls import path
from authorization.views import welcome, login, referral, invalid_token, email_send, auth_token

urlpatterns = [
    path('welcome/', welcome, name="welcome"),
    path('login/', login, name="login"),
    path('referral/', referral, name="referral"),
    path('invalid/', invalid_token, name="invalid_token"),
    path('sended/', email_send, name="email_send"),
    
    path('token/<str:uidb64>/<str:token>/', auth_token, name='auth_token'),
]