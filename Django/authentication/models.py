from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields.related import OneToOneField
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from .managers import SiteUserManager
import uuid
from django.dispatch import receiver
from django.db.models.signals import post_save
from .roles import ADMIN, MEMBER,STARTUP,ROLE_CHOICES
# Create your models here.

class SiteUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    # is_staff = None
    # is_superuser = None 
    uid = models.UUIDField(unique=True,editable=False,default=uuid.uuid4, verbose_name='Public Identifier')
    email = models.EmailField(unique=True)
    role = models.PositiveIntegerField(choices=ROLE_CHOICES,default=3)
    contact_number = models.PositiveIntegerField(default=0,blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']
    objects= SiteUserManager()

    def __str__(self):
        return self.email

class AdminUser(models.Model):
    user = models.OneToOneField(SiteUser, on_delete=CASCADE, related_name='admin_user')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['first_name','last_name']
    def __str__(self):
        return self.first_name +' '+ self.last_name if self.first_name or self.last_name else str(self.user.uid)

class Startup(models.Model):
    # details of the registrar
    # founder_name = models.CharField(max_length=50)
    # founder_pan_id = models.CharField(max_length=20)

    # company details
    user = models.OneToOneField(SiteUser,on_delete=CASCADE, related_name='startup_user')
    gstin = models.CharField(max_length=15, unique=True,blank=False,null=False)
    pan = models.CharField(max_length=16, blank=True)
    company_name = models.CharField(max_length=128,blank=False,null=False)
    description = models.TextField(max_length=2048)
    location = models.CharField(max_length=1024)
    # contact_no = models.CharField(max_length=10)  # validation should be added in forms
    date_of_creation = models.DateField(default=timezone.now)
    industry = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    team_size = models.IntegerField(default=1)
    website = models.URLField(max_length=512,blank=True)
    # company_code = models.CharField(default = ''.join((choice(string.ascii_uppercase) for x in range(7))), unique=True,max_length=7) #this will be used as team-code
    REQUIRED_FIELDS = ['gstin','company_name']

    # objects = StartupManager()
    def __str__(self):
        return self.company_name if self.company_name else str(self.user.uid)


class Member(models.Model):
    # profile_picture = models.ImageField(upload_to="employee_pic/", null=True, blank=True)
    user = models.OneToOneField(SiteUser,on_delete=CASCADE, related_name='member_user')
    startup = models.ForeignKey(Startup, on_delete=RESTRICT,default=None,null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # dob = models.DateField()
    job_title = models.CharField(max_length=50)  # position in the company
    joining_date = models.CharField(max_length=50, default=timezone.now)
    # joining_code = models.CharField(max_length=7)
    REQUIRED_FIELDS = ['first_name','last_name','startup']

    def __str__(self):
        return str(self.first_name + ' ' +self.last_name + ' | '+ self.job_title) if self.first_name or self.last_name or self.job_title else str(self.user.uid)


@receiver (post_save, sender=SiteUser)
def create_user_profile(sender, instance, created, **kwargs):
    print('****', created)
    if instance.role == STARTUP:
        print(instance)
        # instance.company_code = ''.join((choice(string.ascii_uppercase) for x in range(7)))
        Startup.objects.get_or_create(user = instance)
    elif instance.role == ADMIN:
        # print(instance)
        instance.is_superuser = True
        instance.is_staff = True
        AdminUser.objects.get_or_create(user = instance)
    elif instance.role == MEMBER:
        Member.objects.get_or_create(user = instance)

@receiver(post_save, sender=SiteUser)
def save_user_profile(sender, instance, **kwargs):
    print('-----')
    print(instance)
    if instance.role == STARTUP:
        instance.startup_user.save()
    elif instance.role == ADMIN:
        instance.admin_user.save()
    elif instance.role == MEMBER:
        instance.member_user.save()

class PaymentMethod(models.Model):
    startup = models.ForeignKey(Startup,on_delete=CASCADE)
    account_number = models.CharField(max_length=15)
    ifsc = models.CharField(max_length=10)
    account_holders_name = models.CharField(max_length=128)
    upi_id = models.CharField(max_length=256,blank=True,default='')

    def __str__(self):
        return self.account_holders_name 

class Rating(models.Model):
    startup = models.ForeignKey(Startup,on_delete=CASCADE)
    reviewer = models.ForeignKey(Member,on_delete=CASCADE)
    rating = models.PositiveSmallIntegerField(help_text='0-bad to 5-excellent')
    review = models.TextField(max_length=1024)

    def __str__(self):
        return self.startup.company_name

