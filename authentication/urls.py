from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    # path('submit',views.submit,name="submit"),
    path('verify',views.verify, name ="verify"),
]