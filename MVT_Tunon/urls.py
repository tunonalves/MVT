from django.urls import path
from MVT_Tunon import views
urlpatterns = [
    path('',views.inicio),
    path('familiares',views.familiares),
]