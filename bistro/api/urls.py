from django.urls import path

urlpatterns = [
    path('json/', getData(), name='restaurant data')
]