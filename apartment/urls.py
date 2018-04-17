from django.conf.urls import url

urlpatterns=[
    url(r'^all/','apartment.views.show_all'),
    url(r'^rent/$','apartment.views.show_rent'),
    url(r'^setrent/$','apartment.views.setRent'),
]