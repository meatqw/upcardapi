from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from api.models import Account
from services.send_message_service import SendMsg


def welcome(request):
    """Wlcome page"""
    context = {
        "page_info": ""
    }
    return render(request, 'authorization/start.html', context)


def email_send(request):
    """Email is send"""
    context = {
        "page_info": ""
    }
    return render(request, 'authorization/email-sended.html', context)


def invalid_token(request):
    """invalidToken page"""
    context = {
        "page_info": ""
    }
    return render(request, 'authorization/invalid.html', context)


def login(request):
    """login page"""

    context = {
        "page_info": "Подтверждение Email"
    }

    auth_url = ''
    if request.method == 'POST':
        email = request.POST['email']
        user = Account.objects.filter(email=email).first()
        if not user:
            user = Account(email=email).save()
            user = Account.objects.filter(email=email).first()
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            # создаем постоянную ссылку авторизации
            auth_url = reverse('auth_token', kwargs={'uidb64': uidb64, 'token': token})
            auth_url = request.build_absolute_uri(auth_url)
            try:
                SendMsg.send_message_email_welcome(email=email, link=auth_url)
            except Exception as e:
                pass
            return redirect('/auth/sended/')
        else:
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            # создаем постоянную ссылку авторизации
            auth_url = reverse('auth_token', kwargs={'uidb64': uidb64, 'token': token})
            auth_url = request.build_absolute_uri(auth_url)

            try:
                SendMsg.send_message_email_welcome(email=email, link=auth_url)
            except Exception as e:
                pass
            return redirect('/auth/sended/')

    return render(request, 'authorization/confirmation.html', context)


def referral(request):
    """Referral auth page"""
    context = {
        "page_info": "Введите реферальную ссылку"
    }

    return render(request, 'authorization/confirmation-referral.html', context)


@csrf_exempt
def auth_token(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user and PasswordResetTokenGenerator().check_token(user, token):
        account = Account.objects.get(pk=user.id)
        account.token = token
        account.save()

        domain = 'https://my.upcard.online'
        # domain = 'http://localhost:1024/'

        response = redirect(f'{domain}/load?token=%s' % token)
        return response
    else:
        return redirect('/auth/invalid/')
