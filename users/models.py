from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

import uuid

# 客製化 User Model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=150, unique=True)

    email = models.EmailField(_("email address"), unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    #region (Custom Field)
    phone_number = models.IntegerField("手機號碼", unique=True, null=True, blank=True)
    birthday = models.DateField("生日", null=True, blank=True)
    #endregion


    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
        ordering = ('date_joined',)