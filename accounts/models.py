from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('Please, enter a Valid email Address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('is_staff should be set to True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('is_superuser should be set to true'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email_address'), unique=True, blank=False)
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Use your country code")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    uuid = models.CharField(max_length=20, unique=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager

    def __str__(self):
        return self.email