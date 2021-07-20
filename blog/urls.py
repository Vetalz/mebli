from django.urls import path
from .views import index, article

urlpatterns = [
    path('', index, name='blog'),
    path('<slug:article_slug>/', article, name='article')
]
