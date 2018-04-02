# coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from customAuth.models import Users_profile,Location
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

    return redirect('')


def showRegister(request):
    data = {
        'title': "Register",
        'status': "Success",
    }
    return render(request,'authTemplate/register.html',context=data)

def register(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    email = request.POST.get('email','')
    confirm = request.POST.get('password_confirmation','')
    if password != confirm:
        data = {
            'title':'注册',
            'status':'error',
            'message':'您前后两次输入的密码不一致，请重新输入'
        }
        return redirect('/auth/register',data)

    user = User.objects.create_user(username=username,email=email,password=password)
    user.first_name = request.POST.get('first-name')
    user.last_name=request.POST.get('last-name')
    user.save()
    login(request,user)
    data = {
        'title': '首页',
        'status': 'success',
        'user':user
    }
    return redirect('/auth/showsetprofile',data)

def userLogout(request):
    logout(request)
    return redirect('')


def showIndex(request):
    data = {
        'title': '首页',
        'status': 'success'
    }
    return render(request, 'index.html', context=data)


def showSetProfile(request):
    pass

def setProfile(request):
    pass

def showProfile(request,user_id):
    pass