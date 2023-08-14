from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .subscription import Subscription
from .account_manager import AccountManager


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=200, null=True, blank=True)
    id_subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def last_login(self):
        return None
