
from django.urls import path
from .import views

urlpatterns = [
   
    path('pages/index', views.index, name='index'),
    path('pages/about', views.about, name='about'),

]
