from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.provider_list, name='provider_list'),
]