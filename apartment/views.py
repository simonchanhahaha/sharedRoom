from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from apartment.models import Subway, Apartment, Garden, ApartmentImg
from customAuth.models import Location, Users_profile
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from order.models import Star


def index(request):
    user = request.user
    location = user.users_profile.location
    apartments = Apartment.objects.filter(is_rent=False)
    hezu = apartments.filter(rent_type=False).all().reverse()
    zhengzu = apartments.filter(rent_type=True).all().reverse()

    lists_1 = hezu[0:3]
    lists_2 = hezu[4:7]
    lists_3 = zhengzu[0:3]
    lists_4 = zhengzu[4:7]

    hots_lists = Apartment.objects.filter(is_rent=False).order_by("-views").all()
    hots = hots_lists[0:3]
    data = {
        'title': '首页',
        'status': 'success',
        'location': location,
        'lists_1': lists_1,
        'lists_2': lists_2,
        'lists_3': lists_3,
        'lists_4': lists_4,
        'hots': hots
    }
    return render(request, 'welcome.html', context=data)


def return_page_apartment(page, obj):
    paginator = Paginator(obj, 20)

    if page:
        return paginator.page(page).object_list
    else:
        return paginator.page(1).object_list


def return_pages(page, obj):
    paginator = Paginator(obj, 20)

    try:
        pages = paginator.page(page)
        return pages
    except PageNotAnInteger:
        pages = paginator.page(1)
        return pages
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)
        return pages


def showIndex(request):
    user = request.user
    location = user.users_profile.location
    apartments_all = Apartment.objects.filter(is_rent=False).all().reverse()
    apartments_hezu = Apartment.objects.filter(is_rent=False).filter(rent_type=False).all().reverse()
    apartments_zhengzu = Apartment.objects.filter(is_rent=False).filter(rent_type=True).all().reverse()
    count_all = len(apartments_all)
    count_hezu = len(apartments_hezu)
    count_zhengzu = len(apartments_zhengzu)

    page = request.GET.get('page')

    apartment_all = return_page_apartment(page, apartments_all)
    pages_all = return_pages(page, apartments_all)
    apartment_hezu = return_page_apartment(page, apartments_hezu)
    pages_hezu = return_pages(page, apartments_hezu)
    apartment_zhengzu = return_page_apartment(page, apartments_zhengzu)
    pages_zhengzu = return_pages(page, apartments_zhengzu)

    data = {
        'title1': '列表页-',
        'status': 'success',
        'location': location,
        'apartment_all': apartment_all,
        'apartment_hezu': apartment_hezu,
        'apartment_zhengzu': apartment_zhengzu,
        'count_all': count_all,
        'count_hezu': count_hezu,
        'count_zhengzu': count_zhengzu,
        'pages_all': pages_all,
        'pages_hezu': pages_hezu,
        'pages_zhengzu': pages_zhengzu,
    }
    return render(request, 'index.html', context=data)


def show_city(request, id):
    city = Location.objects.filter(id=id).first()
    if city is not None:
        apartments_all = []
        apartments_hezu = []
        apartments_zhengzu = []
        if len(city.location_set.all()) != 0:
            garden_lists = []
            for city_tmp in city.location_set.all():
                garden_lists.extend(city_tmp.garden_set.all())
        else:
            garden_lists = city.garden_set.all()
        for garden in garden_lists:
            apartments = garden.apartment_set.filter(is_rent=False).all()
            apartments_all.extend(apartments)

        for apartment in apartments_all:
            if apartment.rent_type is True:
                apartments_zhengzu.append(apartment)
            else:
                apartments_hezu.append(apartment)

        user = request.user
        location = user.users_profile.location

        count_all = len(apartments_all)
        count_hezu = len(apartments_hezu)
        count_zhengzu = len(apartments_zhengzu)

        page = request.GET.get('page')

        apartment_all = return_page_apartment(page, apartments_all)
        pages_all = return_pages(page, apartments_all)
        apartment_hezu = return_page_apartment(page, apartments_hezu)
        pages_hezu = return_pages(page, apartments_hezu)
        apartment_zhengzu = return_page_apartment(page, apartments_zhengzu)
        pages_zhengzu = return_pages(page, apartments_zhengzu)

        data = {
            'title1': '列表页-',
            'status': 'success',
            'location': location,
            'apartment_all': apartment_all,
            'apartment_hezu': apartment_hezu,
            'apartment_zhengzu': apartment_zhengzu,
            'count_all': count_all,
            'count_hezu': count_hezu,
            'count_zhengzu': count_zhengzu,
            'pages_all': pages_all,
            'pages_hezu': pages_hezu,
            'pages_zhengzu': pages_zhengzu,
        }
        return render(request, 'index.html', context=data)
    else:
        return redirect('/')

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
    garden = Garden.objects.filter(name__contains=garden_name)

    if len(garden) != 0:
        garden_id = garden.first()
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
    apartment.views += 1
    apartment.save()
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

    star = Star.objects.filter(user=request.user).filter(apartment=apartment).first()
    context = {
        'title': '[' + apartment.name + ']',
        'id': apartment.id,
        'apartment_name': apartment.name,
        'price': apartment.price,
        'garden_id': apartment.garden_id.id,
        'garden_name': apartment.garden_id.name,
        'location': apartment.garden_id.location_id,
        'p_location': apartment.garden_id.location_id.pid,
        'size': apartment.size,
        'floor': apartment.floor,
        'room': apartment.room,
        'bathroom': apartment.bathroom,
        'hall': apartment.hall,
        'forward': forward,
        'views': apartment.views,
        'decoration': decoration,
        'payment': payment,
        'rent_type': rent_type,
        'created_time': apartment.created_time,
        'apartment_lists': apartment_lists,
        'has_furniture': furniture,
        'pic': apartment.apartmentimg_set.first().img,
        'star_count': apartment.star_set.count(),
        'star': star,
        'description': apartment.description,
        'owner': apartment.user_id
    }

    return render(request, 'apartment/detail2.html', context=context)
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
