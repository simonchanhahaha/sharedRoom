"""sharedRoom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
                  url(r'^$', 'apartment.views.index'),
                  url(r'search/',include('haystack.urls')),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^auth/', include('customAuth.urls')),
                  url(r'^apartment/', include('apartment.urls')),
                  url(r'^city/(\d+)/', 'apartment.views.city'),
                  url(r'^(\d+)/$', 'apartment.views.show_city'),
                  url(r'^garden/(\d+)/$', 'apartment.views.show_garden'),
                  url(r'^avatar/', 'customAuth.views.avatar'),
                  url(r'^setavatar/', 'customAuth.views.set_avatar'),
                  url(r'^writearticle/$', 'order.views.article'),
                  url(r'^articles/$', 'order.views.show_articles'),
                  url(r'^article/(\d+)/$', 'order.views.show_article'),
                  url(r'^article/(\d+)/delete/$', 'order.views.delete_article'),
                  url(r'^article/(\d+)/showedit/$', 'order.views.show_edit_article'),
                  url(r'^article/(\d+)/edit/$', 'order.views.edit_article'),
                  url(r'^publish/$', 'order.views.handle_article'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
