from django.urls import path
from . import views

urlpatterns = [
    path('enuz/', views.enuz, name = 'enuz'),
    path('uzen/', views.uzen, name = 'uzen')
]
