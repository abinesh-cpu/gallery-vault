from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home',views.home),
    path('register',views.register),
    path('upload_file',views.upload_file),
    path('logout',views.logout)
]