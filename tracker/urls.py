from django.urls import path, include
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.provider_list, name='provider_list'),
    path('doc/impressum/', views.impressum, name='impressum'),
    path('doc/tc/', views.tc, name='tc'),
    path('doc/pp/', views.pp, name='pp'),
    path('doc/contact/', views.contact, name='contact'),
]