from django.contrib import admin
from django.urls import path
from django.urls import include,path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('transiction/',views.transiction,name='transiction'),
    path('make_transiction/<int:id>',views.make_transiction,name="make_transiction"),
    path('transiction_history/',views.transiction_history,name='transiction_history'),
    path('create_user/',views.create_user,name='create_user'),
]