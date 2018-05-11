from django.db import models
from apartment.models import Apartment
from django.contrib.auth.models import User
from customAuth.models import Location

class Star(models.Model):
    user = models.ForeignKey(User,db_column='user_id')
    apartment = models.ForeignKey(Apartment,db_column='apartment_id')


class Order(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    consumer = models.ForeignKey(User)
    apartment = models.ForeignKey(Apartment)
    is_check = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=40,null=False,blank=False)
    requirement = models.TextField(null=False,blank=False)
    location = models.ForeignKey(Location)
    created_date = models.DateTimeField(auto_now_add=True)