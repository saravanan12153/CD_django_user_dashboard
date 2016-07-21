from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="accounts_index"),
    url(r'^signin$', views.signin, name="accounts_signin"),
    url(r'^registerpage$', views.registerpage, name="accounts_registerpage"),
    url(r'^register$', views.register, name="accounts_register"),
    url(r'^logout$', views.logout, name="accounts_logout"),
    url(r'^wall$', views.wall, name="accounts_wall"),
]
