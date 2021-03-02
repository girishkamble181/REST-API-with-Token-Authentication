
from django.contrib import admin
from django.urls import path
from eoapp.views import home
from auapp.views import usignup, ulogin, ulogout, gettoken
from gstapp.views import gst


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('usignup/',usignup, name='usignup'),
    path('ulogin/',ulogin, name='ulogin'),
    path('ulogout/',ulogout, name='ulogout'),
    path('gettoken/',gettoken, name='gettoken'),
    path('gst/',gst),
]
