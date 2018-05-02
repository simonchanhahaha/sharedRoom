from django.conf.urls import url

urlpatterns=[
    url(r'^rent/$','apartment.views.show_rent'),
    url(r'^setrent/$','apartment.views.setRent'),
    url(r'^(\d+)/$','apartment.views.show_detail'),
    url(r'^(\d+)/star','order.views.star')
]