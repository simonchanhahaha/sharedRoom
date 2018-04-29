# coding:utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from customAuth.models import Users_profile, Location, Avatar
from django.http import HttpResponse
import os


def showLogin(request):
    data = {
        'title': '用户登录',
        'status': 'success',
    }
    return render(request, 'authTemplate/login.html', context=data)


def userLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        print('success')

    return redirect('/')


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
    user.first_name = request.POST.get('first-name')
    user.last_name = request.POST.get('last-name')
    user.save()
    login_user = authenticate(username=username, password=password)
    login(request, login_user)
    data = {
        'title': '首页',
        'status': 'success',
        'user': login_user
    }
    return redirect('/auth/showsetprofile/')


def userLogout(request):
    logout(request)
    return redirect('/')



@login_required
def showSetProfile(request):
    return render(request, 'authTemplate/set_profile.html')


@login_required
def setProfile(request):
    user = request.user
    phone = request.POST['phone']
    location = request.POST['location']

    profile = Users_profile()
    profile.user_id = user
    profile.phone = phone
    wechat = request.POST['wechat']

    if wechat is not None:
        profile.wechat = wechat
    else:
        profile.wechat = None

    profile.gender = request.POST['gender']
    profile.location_id = location
    profile.save()

    # '''
    # set avatar
    # '''
    set_avatar(request)
    return redirect('/')


def showProfile(request, user_id):
    user = User.objects.get(id=user_id)
    data = {
        'title': user.username,
        'status': "success",
        'user': user
    }
    return render(request, 'authTemplate/show_profile.html', context=data)


def avatar(request):
    return render(request,'authTemplate/avatar.html')

def set_avatar(request):
    if request.FILES.get('avatar') is not None:
        if request.user.avatar is not None:
            avatar = request.user.avatar
            avatar.version += 1
        else:
            avatar = Avatar()
            avatar.user_id = request.user
        avatar.img = request.FILES['avatar']
        avatar.path = 'avatar/' + str(request.user.id) + '/' + request.FILES['avatar'].name
        avatar.save()
        return HttpResponse(avatar.path)
    else:
        if request.user.avatar is not None:
            return redirect('auth/profile/'+str(request.user.id))
        else:
            avatar = Avatar()
            avatar.user_id = request.user
            avatar.img = 'avatar/default.png'
            avatar.path = 'avatar/default.png'
            avatar.save()
            return HttpResponse(avatar.path)
