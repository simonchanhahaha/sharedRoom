# coding:utf-8
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from customAuth.models import Users_profile, Location, Avatar
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


def showIndex(request):
    if request.user.is_authenticated():
        profile = Users_profile.objects.get(user_id=request.user.id)
        if profile is not None:
            data = {
                'title': '首页',
                'status': 'success',
                'user': request.user
            }
            return render(request, 'index.html', context=data)
        return redirect('/auth/showsetprofile/')
    else:
        data = {
            'title': '首页',
            'status': 'success',
        }
        return render(request, 'index.html', context=data)


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

    # profile.location_id = location
    avatar = request.FILES['avatar']
    if avatar is not None:
        setAvatar(avatar,user)

    return redirect('/')

def showProfile(request, user_id):
    user=User.objects.get(id=user_id)
    data={
        'title':user.username,
        'status':"success",
        'user':user
    }
    return render(request,'authTemplate/show_profile.html',context=data)


def setAvatar(avatar,user):
    avatar_obj = Avatar()
    avatar_name = str(user.id) + '.' + avatar.name.split('.')[-1]

    path = 'avatar/' + str(user.id) + '/'

    if not os.path.exists(path):
        os.mkdir(path)
    with open(path + avatar_name, 'wb+') as pic:
        for chunk in avatar.chunks():
            pic.write(chunk)

    avatar_obj.user_id = user
    avatar_obj.path = path
    avatar_obj.version = 1
    avatar_obj.save()
    return avatar_obj