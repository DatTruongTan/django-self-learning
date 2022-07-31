from django.urls import path
from . import views

# register the app namespace
# URL NAMES
app_name = 'my_app'

urlpatterns = [
    path('', views.example_view, name='example'),
    path('var/', views.variable_view, name='var')
]
