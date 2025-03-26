from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home',views.home),
    path('register',views.register),
    path('logout',views.logout),
    path('gallery_view', views.gallery_view),
    path('delete/<int:image_id>/', views.delete_image),
]