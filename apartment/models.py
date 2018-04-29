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
    company = models.CharField(max_length=30)




class Apartment(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    rent_type = models.BooleanField() #True 整租,False 合租
    size = models.FloatField( null=False, blank=False)
    room=models.SmallIntegerField(default=1)
    hall=models.SmallIntegerField(default=0)
    bathroom=models.SmallIntegerField(default=0)
    floor = models.SmallIntegerField( null=False, blank=False)
    has_furniture=models.BooleanField(default=0,null=False, blank=False)
    decoration_type = models.SmallIntegerField()
    price = models.IntegerField(null=False, blank=False)
    payment_type = models.SmallIntegerField()
    forward = models.SmallIntegerField()
    user_id = models.ForeignKey(User, db_column='user_id')
    garden_id = models.ForeignKey(Garden, db_column='garden_id')
    # subway_id = models.ForeignKey(Subway,db_column='subway_id',default='')
    description = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    is_rent = models.BooleanField(default=0)

def apartment_img_path(instance, filename):
    return '/'.join(['apartment', str(instance.apartment.id), filename])

class ApartmentImg(models.Model):
    apartment = models.ForeignKey(Apartment)
    img = models.ImageField(upload_to=apartment_img_path)

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    apartment_id = models.ForeignKey(Apartment)

# class Image(models.Model):
#