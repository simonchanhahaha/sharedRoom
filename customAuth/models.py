from django.db import models
from django.conf import settings
from time import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class Location(models.Model):
    province = models.CharField(max_length=20, null=False, blank=False)
    pid = models.ForeignKey('self', null=True, blank=True, db_column='pid')


class UsersManager(BaseUserManager):
    def _create_user(self, username, email, password,
                     is_staff, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('Every User must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class Users(AbstractBaseUser):
    username = models.CharField(verbose_name='Username', max_length=20, unique=True, null=False, blank=False)
    email = models.EmailField(verbose_name='Email', unique=True, null=False, blank=False)

    # is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Users_profile(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.BooleanField(default=0, null=False, blank=False)
    phone = models.CharField(max_length=11, null=False, blank=False)
    wechat = models.CharField(max_length=20, null=True, blank=True)
    location = models.ForeignKey(Location)
