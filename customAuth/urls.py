from django.conf.urls import url

urlpatterns=[
    url(r'^showlogin/$','customAuth.views.showLogin'),
    url(r'^login/$','customAuth.views.userLogin'),
    url(r'^showregister/$','customAuth.views.showRegister'),
    url(r'^register/$','customAuth.views.register'),
    url(r'^logout/$','customAuth.views.userLogout'),
    url(r'^showsetprofile/$','customAuth.views.showSetProfile'),
    url(r'^setprofile/$','customAuth.views.setProfile'),
    url(r'^profile/(\d+)','customAuth.views.showProfile')
]