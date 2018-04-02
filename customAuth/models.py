from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    province = models.CharField(max_length=20, null=False, blank=False)
    pid = models.ForeignKey('self', null=True, blank=True, db_column='pid')



class Users_profile(models.Model):
    user_id = models.OneToOneField(User,db_column='user_id')
    gender = models.BooleanField(default=0, null=False, blank=False)
    phone = models.CharField(max_length=11, null=False, blank=False)
    wechat = models.CharField(max_length=20, null=True, blank=True)
    location = models.ForeignKey(Location)
