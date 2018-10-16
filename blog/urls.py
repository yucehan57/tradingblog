from django.urls import path
from . import views

urlpatterns = [
    # ex /blog/
    path('', views.home, name='blog-home'),
    # ex /blog/about
    path('about/', views.about, name='blog-about'),
    # ex /blog/contact
    path('contact/', views.contact, name='blog-contact'),


]

