# coding:utf-8
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def showLogin(request):
    data={
        'title':'用户登录',
        'status':'success',
    }
    return render(request,'authTemplate/login.html',context=data)

def userLogin(request):
    username = request.POST.get['username']
    password = request.POST.get['password']
    login(request)


def showRegister(request):
    pass

def register(request):
    pass

def userLogout(request):
    pass

def showIndex(request):
    data={
        'title':'首页',
        'status':'success'
    }
    return render(request,'index.html',context=data)