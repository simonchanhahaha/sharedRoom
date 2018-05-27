# coding:utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from customAuth.models import Users_profile, Location, Avatar
from order.models import Star,Article
from apartment.models import Apartment
import os


def showLogin(request):
    request.session['last_url'] = request.META.get('HTTP_REFERER','/')
    data = {
        'title': '用户登录',
        'status': 'success',
    }
    return render(request, 'authTemplate/login.html', context=data)


def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    url = request.session.get('last_url','/')
    del request.session['last_url']
    if user.is_authenticated():
        login(request, user)
        print('success')

        return redirect(url)
    else:
        return redirect('/auth/showlogin')


def showRegister(request):
    data = {
        'title': "Register",
        'status': "Success",
    }
    return render(request, 'authTemplate/register.html', context=data)


def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    email = request.POST.get('email', '')
    confirm = request.POST.get('password_confirmation', '')
    if password != confirm:
        data = {
            'title': '注册',
            'status': 'error',
            'message': '您前后两次输入的密码不一致，请重新输入'
        }
        return redirect('/auth/register', data)

    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = request.POST.get('first-name','')
    user.last_name = request.POST.get('last-name','')
    user.save()
    login_user = authenticate(username=username, password=password)
    login(request, login_user)
    data = {
        'title': '填写个人信息',
        'status': 'success',
        'user': login_user
    }
    return redirect('/auth/showsetprofile/',data)


def userLogout(request):
    url = request.META.get('HTTP_REFERER','/')
    logout(request)
    return redirect(url)


@login_required
def showSetProfile(request):
    return render(request, 'authTemplate/set_profile.html')


@login_required
def setProfile(request):
    user = request.user
    phone = request.POST.get('phone','')
    location_id = request.POST.get('location','')
    location = Location.objects.filter(id=location_id).first()
    wechat = request.POST.get('wechat','')

    profile = Users_profile()
    profile.user_id = user
    profile.phone = phone
    profile.wechat = wechat

    profile.gender = request.POST.get('gender','')
    profile.location= location

    avatar = request.FILES.get('avatar','')
    result = set_avatar(avatar,request.user)
    profile.save()

    return redirect('/')

@login_required
def showProfile(request, user_id):
    if str(request.user.id) != str(user_id):
        return redirect('/')
    else:
        user = request.user
        star_lists = Star.objects.filter(user=user)
        star_apartments = []
        for star in star_lists:
            star_apartments.append(star.apartment)

        apartments = Apartment.objects.filter(user_id=user)
        articles = request.user.article_set.all()
        data = {
            'title': user.username,
            'status': "success",
            'user': user,
            'star_apartments':star_apartments,
            'articles':articles,
            'apartments':apartments
        }
        return render(request, 'authTemplate/show_profile.html', context=data)


def avatar(request):
    return render(request, 'authTemplate/avatar.html')


def set_avatar(get_avatar,user):
    if get_avatar != '':
        avatar = Avatar()
        avatar.user_id = user
        avatar.img = avatar
        avatar.path = 'avatar/' + str(user.id) + '/' + get_avatar.name
        avatar.save()
    else:
        avatar = Avatar()
        avatar.user_id = user
        avatar.img = 'avatar/default.png'
        avatar.path = 'avatar/default.png'
        avatar.save()
    return avatar