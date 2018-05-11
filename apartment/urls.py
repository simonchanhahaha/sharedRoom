from django.conf.urls import url

urlpatterns=[
    url(r'^hezu$','apartment.views.show_hezu'),
    url(r'^zhengzu$','apartment.views.show_zhengzu'),
    url(r'^renzheng$','apartment.views.show_renzheng'),
    url(r'^showrent/$','apartment.views.show_rent'),
    url(r'^rent/$','apartment.views.rent_handle'),
    url(r'^(\d+)/$','apartment.views.show_detail'),
    url(r'^(\d+)/star','order.views.star'),
    url(r'^(\d+)/showupdate','apartment.views.show_update'),
    url(r'^(\d+)/update','apartment.views.update_handle'),
    url(r'^(\d+)/delete','apartment.views.delete_handle'),
]