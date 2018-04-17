from django.db import models
from customAuth.models import Location
from django.contrib.auth.models import User


# Create your models here.

class Subway(models.Model):
    line = models.CharField(max_length=10,blank=False, null=False)
    station = models.CharField(max_length=10, blank=False, null=False)
    locaition_id = models.ForeignKey(Location,db_column='location_id')
    class Meta:
        db_table = 'subway'


class Garden(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    location_id = models.ForeignKey(Location, db_column='location_id')
    description = models.TextField()
    company = models.CharField(max_length=30)


class Apartment(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    rent_type = models.BooleanField()
    size = models.FloatField( null=False, blank=False)
    room=models.SmallIntegerField(default=1)
    hall=models.SmallIntegerField(default=0)
    bathroom=models.SmallIntegerField(default=0)
    floor = models.SmallIntegerField( null=False, blank=False)
    has_furniture=models.BooleanField(default=0,null=False, blank=False)
    decoration_type = models.SmallIntegerField()
    price = models.IntegerField(null=False, blank=False)
    payment_type = models.SmallIntegerField()
    forward = models.CharField(max_length=10)
    user_id = models.ForeignKey(User, db_column='user_id')
    garden_id = models.ForeignKey(Garden, db_column='garden_id')


class Tag(models.Model):
    tag = models.CharField(max_length=20)
    apartment_id = models.ForeignKey(Apartment)

# class Image(models.Model):
#