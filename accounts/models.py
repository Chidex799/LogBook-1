from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db.models.deletion import CASCADE
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
import uuid
from django.core.mail import send_mail
# Create your models here.

UNIVERSITIES_CHOICES = (
    ('ABSU', 'Abia State University'),
    ('AUO', 'Achievers University'),
    ('ADSU', 'Adamawa State University'),
    ('AAUA', 'Adekunle Ajasin University'),
    ('AU', 'Adeleke University'),
    ('ADUN', 'Admiralty University of Nigeria'),
    ('ABUAD', 'Afe Babalola University'),
    ('AUST', 'African Univeristy of Science and Technology'),
    ('ABUZARIA', 'Ahmadu Bello University'),
    ('ACU', 'Ajayi Crowther University'),
    ('AKSU', 'Akwa Ibom State University'),
    ('FUNAI', 'Alex Ekwueme Federal University, Ndufu-Alike'),
    ('HUI', 'Al-Hikmah University'),
    ('AUK', 'Al-Qalam University, Katsina'),
    ('AAU', 'Ambrose Ali University'),
    ('AUN', 'American University of Nigeria'),
    ('AUL', 'Anchor University, Lagos'),
    ('AJU', 'Arthur Jarvis University'),
    ('ATU', 'Atiba University'),
    ('AU', 'Augustine University'),
    ('BABCOCK', 'Babcock University'),
    ('BASUG', 'Bauchi State University'),
    ('BUK', 'Bayero University Kano'),
    ('BAZE', 'Baze University'),
    ('BUT', 'Bells University of Technology'),
    ('BIU', 'Benson Idahosa University'),
    ('BSU', 'Benue State University'),
    ('BUN', 'Bingham University'),
    ('BSU', 'Borno State University'),
    ('BU', 'Bowen University'),
    ('CUL', 'Caleb University'),
    ('CU', 'Caritas University'),
    ('CHRISLAND', 'Chrisland University'),
    ('Cu', 'Christopher University'),
    ('COOU', 'Chukwuemeka Odumegwu Ojukwu University'),
    ('CLU', 'Clifford University'),
    ('CCU', 'Coal City University'),
    ('CU', 'Convenant University'),
    ('cu', 'Crawford University'),
    ('cu', 'Crescent University, Abeokuta'),
    ('CRUTECH', 'Cross River University of Technology'),
    ('CHU', 'Crown Hill University'),
    ('DELSU', 'Delta State University, Abraka'),
    ('DU', 'Dominican University, Ibadan'),
    ('EPU', 'Eastern Palm University'),
    ('EBSU', 'Ebonyi State University'),
    ('EDSU', 'Edo State University, Iyamho'),
    ('ECU', 'Edwin Clark University'),
    ('EKSU', 'Ekiti State University, Ado Ekiti'),
    ('EKOUNIVMED', 'Eko University of Medical and Health Sciences'),
    ('EUI', 'Elizade University'),
    ('ESUTECH', 'Enugu State University of Science and Technology'),
    ('EUA', 'Evangel University, Akaeze'),
    ('FUNAAB', 'Federal University of Agriculture, Abeokuta'),
    ('FUPREM', 'Federal University of Petroleum Resources'),
    ('FUTA', 'Federal University of Technology, Akure'),
    ('FUTMINNA', 'Federal University of Technology, Minna'),
    ('FUTO', 'Federal University of Technology, Owerri'),
    ('FUBK', 'Federal University, Birnin Kebbi'),
    ('FUD', 'Federal University, Dutse'),
    ('FUDMA', 'Federal University, Dutsin-Ma'),
    ('FUG', 'Federal University, Gashua'),
    ('FUGUS', 'Federal University, Gusau'),
    ('FUK', 'Federal University, Kashere'),
    ('FULafia', 'Federal University, Lafia'),
    ('FUL', 'Federal University, Lokoja'),
    ('FUTOTUOKE', 'Federal University, Otuoke'),
    ('FUOYE', 'Federal University, Oye-Ekiti'),
    ('FUWUAKRI', 'Federal University, Wukari'),
    ('FUO', 'Fountain University, Osogbo'),
    ('GVU', 'Glorious Vision University'),
    ('GOU', 'Godfrey Okoye University'),
    ('GSU', 'Gombe State University'),
    ('GSUST', 'Gombe State University of Science and Technology'),
    ('GUU', 'Gregory University, Uturu'),
    ('Hallmark', 'Hallmark University, Ijebu-Itele'),
    ('HU', 'Hezekiah University'),
    ('IBBUL', 'Ibrahim Badamasi Babangida University'),
    ('IUO', 'Igbinedion University Okada'),
    ('IAUE', 'Ignatius Ajuru University of Education'),
    ('IMSU', 'Imo State University'),
    ('JABU', 'Joseph Ayo Babalola University'),
    ('KASU', 'Kaduna State University'),
    ('KUST', 'Kano University of Science and Technology'),
    ('KSUSTA', 'Kebbi State University of Science and Technology'),
    ('KU', 'Kings University'),
    ('KSU', 'Kogi State University'),
    ('KDU', 'Kola Daisi University'),
    ('KWASU', 'Kwara State University'),
    ('KWU', 'Kwararafa University, Wukari'),
    ('LAUTECH', 'Ladoke Akintola University of Technology'),
    ('LASU', 'Lagos State University'),
    ('LMU', 'Landmark University'),
    ('LCU', 'Lead City University'),
    ('LUO', 'Legacy University, Okija'),
    ('MU', 'Madonna University, Okija'),
    ('McU', 'Mcpherson University'),
    ('MCIU', 'Michael and Cecilia Ibru University'),
    ('MOUAU', 'Michael Okpara University of Agriculture'),
    ('MAUTECH', 'Modibbo Adama University of Technology'),
    ('MAUSTECH', 'Moshood Abiola University of Science and Technology, Abeokuta'),
    ('MTU', 'Mountain Top University'),
    ('NSUK', 'Nasarawa State University'),
    ('NDU', 'Niger Delta University'),
    ('NMU', 'Nigerian Maritime University, Okerenkoko'),
    ('Nile', 'Nile University of Nigeria'),
    ('UNIZIK', 'Nnamdi Azikiwe University'),
    ('Novena', 'Novena University'),
    ('OAU', 'Obafemi Awolowo University'),
    ('OUO', 'Obong University'),
    ('OUI', 'Oduduwa University'),
    ('OOU', 'Olabisi Onabanjo University'),
    ('OSUTECH', 'Ondo State University of Science and Technology'),
    ('PUMS', 'PAMO University of Medical Sciences'),
    ('PAU', 'Pan-Atlantic University'),
    ('PUA', 'Paul University'),
    ('PLASU', 'Plateau State University'),
    ('PCU', 'Precious Cornerstone University'),
    ('RUN', 'Redeemer\'s University'),
    ('RUE', 'Renaissance University'),
    ('RU', 'Rhema University'),
    ('RU', 'Ritman University'),
    ('RSU', 'Rivers State University'),
    ('SU', 'Salem University'),
    ('SUN', 'Skyline University Nigeria'),
    ('SSU', 'Sokoto State University'),
    ('SUN', 'Southwestern University, Nigeria'),
    ('SUN', 'Spiritan University, Nneochi'),
    ('SLU', 'Sule Lamido University'),
    ('SUO', 'Summit University Offa'),
    ('TASUED', 'Tai Solarin University of Education'),
    ('TANU', 'Tansian University'),
    ('TSU', 'Taraba State University'),
    ('TTU', 'The Technical University'),
    ('UMYU', 'Umaru Musa Yar\'Adua University'),
    ('UNIABUJA', 'University of Abuja'),
    ('UOA', 'University of Africa'),
    ('UAM', 'University of Agriculture, Makurdi'),
    ('UNIBEN', 'University of Benin'),
    ('UNICAL', 'University of Calabar'),
    ('UI', 'University of Ibadan'),
    ('UNIILORIN', 'University of Ilorin'),
    ('UNIJOS', 'University of Jos'),
    ('UNILAG', 'University of Lagos'),
    ('UNIMAID', 'University of Maiduguri'),
    ('UCMS', 'University of Medical Sciences'),
    ('UMM', 'University of Mkar'),
    ('UNN', 'University of Nigeria'),
    ('UNIPORT', 'University of Port Harcourt'),
    ('UNIUYO', 'University of Uyo'),
    ('UDUS', 'Usmanu Danfodio University'),
    ('VU', 'Veritas University'),
    ('WU', 'Wellspring University'),
    ('WUSTO', 'Wesley University of Science and Technology'),
    ('WDU', 'Western Delta University'),
    ('YSU', 'Yobe State University'),
    ('YUMSUK', 'Yusuf Maitama Sule University Kano'),
    ('ZSU', 'Zamfara State University'),
)

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

class Universities(models.Model):
    university_choices = models.CharField(choices=UNIVERSITIES_CHOICES, default="ABSU", blank=False)     
        
class InstitutionSupervisor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    institution=models.CharField(max_length=254)
    
    def __str__(self):
        return self.user.email

class UniversitySupervisor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.ForeignKey(Universities, on_delete=models.CASCADE)
    #  universiity (foreign  key ): handled by someone
    department = models.CharField(max_length=254)

    def __str__(self):
        return self.user.email

class Students(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    matricNum = models.CharField(max_length=150, null=False)
    InstitutionSupervisor = models.OneToOneField(InstitutionSupervisor, on_delete= models.CASCADE, null= True, blank = True)
    universityInspec = models.OneToOneField(UniversitySupervisor, on_delete= models.CASCADE, null = True, blank = True)
    department = models.CharField(max_length=250, null=False)
    regdate = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    university = models.ForeignKey(Universities, on_delete=models.CASCADE)
    # universiity (foreign  key ): handled by someone
    
    def __str__(self):
        return self.user.email
    