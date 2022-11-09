from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from api.models import Menu_item, Category, Cuisine
from pprint import pprint as pp

# Create your views here.

data = ()


def getData(request):
    menu_items = Menu_item.objects.all()
    JSON_DATA = list()
    if request.method == 'GET':
        for item in menu_items:
            JSON_DATA.append({
                'title': item.title,
                'price': item.price,
                'decription': item.description,
                'spicy_level': item.spicy_level,
                'category': model_to_dict(Category.objects.get(id=item.category_id)),
                'cuisine': model_to_dict(Cuisine.objects.get(id=item.cuisine_id)),
            })

        return JsonResponse({'data': JSON_DATA})
