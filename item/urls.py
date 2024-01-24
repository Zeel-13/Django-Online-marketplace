from django.urls import path
from .views import *
app_name='item'
urlpatterns = [
    path('<int:pk>/',detail,name='detail'),
    path('new/',new,name='new')
]