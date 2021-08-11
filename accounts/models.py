from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
import uuid
from django.core.mail import send_mail
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
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
    username = None
    email = models.EmailField(_('email_address'), unique=True, blank=False)
    first_name = models.CharField(max_length=250, blank=False)
    last_name = models.CharField(max_length=250, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Use your country code")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False)
    uuid = models.UUIDField(_("uuid") ,default=uuid.uuid4, editable=False, unique=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
class InstitutionSupervisor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    institution=models.CharField(max_length=254)
    
class UniversitySupervisor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    university=models.CharField(max_length=254)
    department = models.CharField(max_length=254)
