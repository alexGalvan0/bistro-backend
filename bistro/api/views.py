from django.shortcuts import render
from django.http import JsonResponse
from api.models import Menu_item

# Create your views here.
def getData(request):
    data = list(Menu_item.objects.values())
    return JsonResponse({'data':data})