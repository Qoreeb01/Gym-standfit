from django.urls import path
from Fitlife import views

urlpatterns = [
    path('', views.home, name='home'),
]