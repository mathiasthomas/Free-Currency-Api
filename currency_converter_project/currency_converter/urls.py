from django.urls import path
from . import views

urlpatterns = [
    path('conversion-rates/', views.conversion_rates, name='conversion_rates'),
]
