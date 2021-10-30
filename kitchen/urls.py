from django.urls import path
from .views import index, quiz


urlpatterns = [
    path('', index, name='home'),
    path('quiz/', quiz, name='quiz'),
]
