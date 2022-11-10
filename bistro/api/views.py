from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from api.models import Menu_item, Category, Cuisine
from pprint import pprint as pp
from django.views.decorators.http import require_http_methods


# Create your views here.



@require_http_methods(["GET"])
def getData(request):
    JSON_DATA = list()
    menu_items = Menu_item.objects.all()


    for item in menu_items:
        JSON_DATA.append({
            'title': item.title,
            'price': item.price,
            'description': item.description,
            'spicy_level': item.spicy_level,
            'category': model_to_dict(Category.objects.get(id=item.category_id)),
            'cuisine': model_to_dict(Cuisine.objects.get(id=item.cuisine_id)),
        })

    return JsonResponse(JSON_DATA,safe=False)
