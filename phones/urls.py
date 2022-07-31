from django.urls import path
from . import views

app_name = 'phones'

urlpatterns = [
    path('rental_review/', views.rental_view, name='rental_review'),
    path('thank/', views.thank_view, name='thank'),
]