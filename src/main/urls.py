from django.urls import path
from .views import index


app_name = 'index'

urlpatterns = [
    path('index/', index, name='index')
]
