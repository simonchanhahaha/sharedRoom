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
    views = models.IntegerField(default=1)
    requirement = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    is_rent = models.BooleanField(default=0)

    def get_str_decoration(self):
        '''
        获取装修情况描述
        get decoration situation description
        :param self:
        :return:
        '''
        if self.decoration_type == 1:
            decoration = '毛坯'
        elif self.decoration_type == 2:
            decoration = '简单装修'
        elif self.decoration_type == 3:
            decoration = '中等装修'
        elif self.decoration_type == 4:
            decoration = '精装修'
        elif self.decoration_type == 5:
            decoration = '豪华装修'
        else:
            decoration = '其他'

        return decoration

    def get_str_forward(self):
        '''
        获取房屋朝向描述
        get apartment forward description
        :param self.forward:
        :return:
        '''
        if self.forward == 1:
            forward = '东'
        elif self.forward == 2:
            forward = '南'
        elif self.forward == 3:
            forward = '西'
        elif self.forward == 4:
            forward = '北'
        elif self.forward == 5:
            forward = '东北'
        elif self.forward == 6:
            forward = '西北'
        elif self.forward == 7:
            forward = '东南'
        elif self.forward == 8:
            forward = '西南'
        else:
            forward = '不知道房屋朝向'

        return forward

def apartment_img_path(instance, filename):
    return '/'.join(['apartment', str(instance.apartment.id), filename])

class ApartmentImg(models.Model):
    apartment = models.ForeignKey(Apartment)
    img = models.ImageField(upload_to=apartment_img_path)

class Tag(models.Model):
    tag = models.CharField(max_length=20)
    apartment_id = models.ForeignKey(Apartment)

