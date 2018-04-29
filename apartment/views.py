from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apartment.models import Subway, Apartment, Garden,ApartmentImg
from customAuth.models import Location, Users_profile
from django.contrib.auth.decorators import login_required


def showIndex(request):
    if request.user.is_authenticated():
        profile = Users_profile.objects.get(user_id=request.user.id)
        if profile is not None:
            user = request.user
            location = user.users_profile.location
            apartment_lists = Apartment.objects.filter(is_rent=False).all().reverse()
            count = len(apartment_lists)
            data = {
                'title': '首页',
                'status': 'success',
                'location': location,
                'apartment_lists': apartment_lists,
                'count': count
            }
            return render(request, 'index.html', context=data)
        return redirect('/auth/showsetprofile/')
    else:
        data = {
            'title': '首页',
            'status': 'success',
        }
        return render(request, 'index.html', context=data)


def show_all(request):
    user = request.user
    location_id = user.users_profile.location.id
    # return HttpResponse(location)
    return render()


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
        new_garden.company = request.POST['company']
        new_garden.description = request.POST['description']
        new_garden.save()

        garden_id = new_garden

    rent_type = request.POST['rent_type']

    apartment = Apartment()
    if rent_type == '1':
        apartment.rent_type = True
    else:
        apartment.rent_type = False
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

    a_img = ApartmentImg()
    if request.FILES['img'] is not None:
        a_img.img = request.FILES['img']
    else:
        pass

    a_img.apartment = apartment
    a_img.save()
    address = '/apartment/' + str(apartment.id) + '/'
    return redirect(address)


def show_detail(request, id):
    apartment = Apartment.objects.filter(id=id).first()
    garden = apartment.garden_id
    apartment_lists = garden.apartment_set.all().reverse()

    decoration = get_str_decoration(apartment.decoration_type)
    payment = get_str_payment(apartment.payment_type)
    forward = get_str_forward(apartment.forward)
    if apartment.rent_type is True:
        rent_type = '整租'
    else:
        rent_type = '合租'

    if apartment.has_furniture is True:
        furniture = '有'
    else:
        furniture = '无'

    context = {
        'apartment_name': apartment.name,
        'price': apartment.price,
        'garden_name': apartment.garden_id.name,
        'location': apartment.garden_id.location_id,
        'p_location': apartment.garden_id.location_id.pid,
        'size': apartment.size,
        'floor': apartment.floor,
        'room': apartment.room,
        'bathroom': apartment.bathroom,
        'hall': apartment.hall,
        'forward': forward,
        'decoration': decoration,
        'payment': payment,
        'rent_type': rent_type,
        'created_time': apartment.created_time,
        'apartment_lists': apartment_lists,
        'has_furniture': furniture,
        'pic':apartment.apartmentimg_set.first().img
    }

    return render(request, 'apartment/detail.html', context=context)
    # return HttpResponse(context)


def get_str_forward(apartment_forward):
    '''
    获取房屋朝向描述
    get apartment forward description
    :param apartment_forward:
    :return:
    '''
    if apartment_forward == 1:
        forward = '东'
    elif apartment_forward == 2:
        forward = '南'
    elif apartment_forward == 3:
        forward = '西'
    elif apartment_forward == 4:
        forward = '北'
    elif apartment_forward == 5:
        forward = '东北'
    elif apartment_forward == 6:
        forward = '西北'
    elif apartment_forward == 7:
        forward = '东南'
    elif apartment_forward == 8:
        forward = '西南'
    else:
        forward = '不知道房屋朝向'

    return forward


def get_str_decoration(apartment_decoration_type):
    '''
    获取装修情况描述
    get decoration situation description
    :param apartment_decoration_type:
    :return:
    '''
    if apartment_decoration_type == 1:
        decoration = '毛坯'
    elif apartment_decoration_type == 2:
        decoration = '简单装修'
    elif apartment_decoration_type == 3:
        decoration = '中等装修'
    elif apartment_decoration_type == 4:
        decoration = '精装修'
    elif apartment_decoration_type == 5:
        decoration = '豪华装修'
    else:
        decoration = '其他'

    return decoration


def get_str_payment(payment_type):
    '''
    获取付款方式描述
    get payment_type description
    :param payment_type:
    :return:
    '''
    if payment_type == 1:
        payment = '押一付一'
    elif payment_type == 2:
        payment = '押二付一'
    elif payment_type == 3:
        payment = '押一付三'
    elif payment_type == 4:
        payment = '半年付'
    elif payment_type == 5:
        payment = '年付'
    else:
        payment = '其他'

    return payment


def show_garden(request, id):
    garden = Garden.objects.filter(id=id).first()
    if garden is not None:
        apartment_lists = garden.apartment_set.filter(is_rent=False).all().reverse()
        location = request.user.users_profile.location
        count = len(apartment_lists)
        data = {
            'title': garden.name,
            'status': 'success',
            'location': location,
            'apartment_lists': apartment_lists,
            'user': request.user,
            'count': count
        }
        return render(request, 'index.html', context=data)

    else:
        return redirect('/')


def show_city(request, id):
    city = Location.objects.filter(id=id).first()
    if city is not None:
        apartment_lists = []
        if len(city.location_set.all())!=0:
            garden_lists = []
            for city_tmp in city.location_set.all():
                garden_lists.extend(city_tmp.garden_set.all())
            print("1")
        else:
            print("2")
            garden_lists = city.garden_set.all()
        for garden in garden_lists:
            apartments = garden.apartment_set.all()
            apartment_lists.extend(apartments)
        count = len(apartment_lists)
        location = request.user.users_profile.location
        data = {
            'title': city.province,
            'status': 'success',
            'location': location,
            'apartment_lists': apartment_lists,
            'user': request.user,
            'count': count
        }
        return render(request, 'index.html', context=data)

    else:
        return redirect('/')

