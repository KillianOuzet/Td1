from django.urls import path
from django.views.generic import *
from . import  views
urlpatterns=[
  #path('home',views.home,name='home'),
  path('home/<name>',views.home,name='home'),
  path("home", views.HomeView.as_view()),
  path("about", views.AboutView.as_view(), name="about"),
  path("contact", views.ContactView.as_view(), name="contact"),
  path('product',views.list_products,name='all products'),
  path('product/<id>',views.product_by_Id,name='one product'),
]