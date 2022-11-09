from django.urls import path
from . import views

urlpatterns = [
   path('json/', views.getData, name='restaurant data')
]