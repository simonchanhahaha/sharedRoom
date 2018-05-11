from django.contrib import admin
from apartment.models import Apartment,ApartmentImg,Garden
# Register your models here.


class GardenAdmin(admin.ModelAdmin):
    list_display = ('name','location_id')

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('name','garden_id','user_id')
    fk_fields = ('garden_id',)

class ApartmentImgAdmin(admin.ModelAdmin):
    list_display = ('apartment','img')

admin.site.register(Garden,GardenAdmin)
admin.site.register(Apartment,ApartmentAdmin)
admin.site.register(ApartmentImg,ApartmentImgAdmin)