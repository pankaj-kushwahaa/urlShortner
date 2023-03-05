from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('create/', views.create_url, name="create"),
  path('<str:pk>', views.redirect_url, name="redirect_url"),
  path('custom_create/', views.create_custom, name="custom_create"),
  path('custom_create_url/', views.custom_create_url, name="custom_create_url")

]