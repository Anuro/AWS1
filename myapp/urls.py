# myapp/urls.py
from django.urls import path
from .views import create_data, get_data

urlpatterns = [
    path('create/', create_data, name='create_data'),
    path('get/<int:pk>/', get_data, name='get_data'),
]
