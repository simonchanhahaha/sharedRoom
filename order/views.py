from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from apartment.models import Apartment
from order.models import Order, Star,Article
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from customAuth.models import Location
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

@csrf_exempt
@login_required
def star(request,apartment_id):
    user = request.user
    apartment = Apartment.objects.filter(id=apartment_id).first()


    var = Star.objects.filter(user=user).filter(apartment=apartment)

    if len(var) ==0:
        star = Star()
        star.apartment = apartment
        star.user = user
        star.save()
    else:
        star = var.first()
        star.delete()

    return JsonResponse({
        'status':'success'
    })


@login_required
def article(request):
    context = {
        'title':'我想合租'
    }
    return render(request,'set_article.html',context=context)


def return_page_obj(page, obj):
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



def show_articles(request):
    articles_all = Article.objects.all()
    page = request.GET.get('page')
    articles = return_page_obj(page, articles_all)
    pages= return_pages(page, articles_all)
    context={
        'title':'合租列表',
        'articles':articles,
        'pages':pages,
    }

    return render(request,'articles.html',context=context)

def show_article(request,id):
    article=Article.objects.filter(id=id).first()
    context={
        'title':article.title,
        'article':article
    }
    return render(request,'article.html',context=context)

def show_edit_article(request,id):
    article = Article.objects.filter(id=id).first()
    context={
        'title':'修改-'+article.title,
        'article':article,
        'reset':True
    }
    return render(request,'set_article.html',context=context)

def edit_article(request,id):
    article=Article.objects.filter(id=id).first()
    title = request.POST.get('title', '')
    location_id = request.POST.get('location','')

    requirement = request.POST.get('requirement','').strip()
    if title != '':
        article.title=title
    if location_id !='':
        location = Location.objects.filter(id=location_id).first()
        article.location=location
    if requirement!='':
        article.requirement=requirement

    article.save()

    return redirect('/article/'+str(article.id))


@login_required
def handle_article(request):
    article = Article()
    author = request.user
    location_id = request.POST['location']
    location = Location.objects.filter(id=location_id).first()
    title = request.POST['title']
    requirement = request.POST['requirement'].strip()
    article.title = title
    article.location=location
    article.author=author
    article.requirement=requirement.strip()
    article.save()
    return redirect('/article/'+str(article.id))

@login_required
def delete_article(request,id):
    article = Article.objects.filter(id=id).first()
    article.delete()
    # return JsonResponse({
    #     'status':'success'
    # })

    return redirect('/auth/profile/'+str(request.user.id))