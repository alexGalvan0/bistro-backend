from django.urls import path
from . import views

urlpatterns = [
   path('json/<int:id>', views.getFriendlys, name='restaurant data'),
]