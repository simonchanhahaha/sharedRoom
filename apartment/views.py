from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apartment.models import Subway, Apartment, Garden
from customAuth.models import Location
from django.contrib.auth.decorators import login_required


def show_all(request):
    pass


def city(request, id):
    city = Location.objects.filter(pid=id)
    list = []
    for item in city:
        list.append({
            'id': item.id,
            'place': item.province
        })

    return JsonResponse({'data': list})


@login_required
def show_rent(request):
    return render(request, 'apartment/set_rent.html')


@login_required
def setRent(request):
    user = request.user
    location_id = request.POST['district']
    location = Location.objects.filter(id=location_id).first()
    garden_name = request.POST['garden_name']
    garden = Garden.objects.filter(name__contains=garden_name).first()

    if garden is not None:
        garden_id = garden
    else:
        new_garden = Garden()
        new_garden.name = garden_name
        new_garden.location_id = location
        new_garden.save()
        garden_id = new_garden

    apartment = Apartment()
    apartment.rent_type = True
    apartment.garden_id = garden_id
    apartment.size = request.POST['size']
    apartment.floor = request.POST['floor']
    apartment.room = request.POST['room']
    apartment.hall = request.POST['hall']
    apartment.bathroom = request.POST['bathroom']
    apartment.forward = request.POST['forward']
    apartment.has_furniture = request.POST['furniture']
    apartment.decoration_type = request.POST['decoration_type']
    apartment.price = request.POST['price']
    apartment.payment_type = request.POST['payment_type']
    apartment.user_id = user
    apartment.save()

    # imglists = request.POST.getlist('img')
    address = '/' + str(location.id) + '/' + str(apartment.id) + '/'
    return redirect(address)


def show_detail(request, city, id):
    return render(request, 'apartment/detail.html')


def show_apartment(request, city, id):
    apartment = Apartment.objects.filter(id=id).first()
    garden = apartment.garden_id
    lists = garden.apartment_set.all().reverse()
    if apartment.decoration_type == 1:
        decoration = '毛坯'
    elif apartment.decoration_type == 2:
        decoration = '简单装修'
    elif apartment.decoration_type == 3:
        decoration = '中等装修'
    elif apartment.decoration_type == 4:
        decoration = '精装修'
    elif apartment.decoration_type == 5:
        decoration = '豪华装修'
    else:
        decoration = '其他'

    if apartment.payment_type == 1:
        payment = '押一付一'
    elif apartment.payment_type == 2:
        payment = '押二付一'
    elif apartment.payment_type == 3:
        payment = '押一付三'
    elif apartment.payment_type == 4:
        payment = '半年付'
    elif apartment.payment_type == 5:
        payment = '年付'
    else:
        payment = '其他'

    if apartment.rent_type is True:
        rent_type = '整租'
    else:
        rent_type = '合租'

    context = {
        'apartment_name': apartment.name,
        'price': apartment.price,
        'garden_name': apartment.garden_id.name,
        'location_id':apartment.garden_id.location_id.province,
        'location_pid':apartment.garden_id.location_id.pid.province,
        'size': apartment.size,
        'floor': apartment.floor,
        'room': apartment.room,
        'bathroom': apartment.bathroom,
        'hall': apartment.hall,
        'forward': apartment.forward,
        'decoration': decoration,
        'payment': payment,
        'rent_type':rent_type,
        'created_time':apartment.created_time,
        'apartment_lists':lists
    }

    return render(request, 'apartment/detail.html',context=context)
    # return HttpResponse(context)