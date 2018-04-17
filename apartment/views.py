from django.shortcuts import render
from django.http import HttpResponse
from apartment.models import Subway,Apartment,Garden
from customAuth.models import Location
def show_all(request):
    pass

def show_rent(request):
    return render(request,'apartment/set_rent.html')

def setRent(request):
    user = request.user

    garden_name = request.POST['garden_name']
    garden = Garden.objects.filter(name__contains=garden_name).first()

    if garden is not None:
        garden_id = garden.id
    else:
        new_garden = Garden()
        new_garden.name=garden_name
        new_garden.location_id = user.profile.location_id
        # Garden.save()
        garden_id = new_garden.id

    apartment = Apartment()
    apartment.garden_id =garden_id
    apartment.size = request.POST['size']
    apartment.floor = request.POST['floor']
    apartment.forward = request.POST['forward']
    apartment.has_furniture = request.POST['furniture']
    apartment.decoration_type = request.POST['decoration_type']
    apartment.price = request.POST['price']
    apartment.payment_type = request.POST['payment_type']



    # imglists = request.POST.getlist('img')

    return HttpResponse(apartment)