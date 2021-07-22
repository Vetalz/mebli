from django.urls import path
from .views import peretyazhka

urlpatterns = [
    path('', peretyazhka, name='peretyazhka'),
]