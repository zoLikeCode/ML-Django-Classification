from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_url'),
    path('', views.index, name='index_post'),
]
