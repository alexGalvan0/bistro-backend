import json
from pprint import pprint as pp

import requests
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from api.models import Category, Cuisine, Menu_item

# Create your views here.



@require_http_methods(["GET"])
def getFriendlys(request, id):
    JSON_DATA = list()
    if id != 0:
        menu_items = Menu_item.objects.filter(restaurant_id=id)
    elif id == 0:
        menu_items = Menu_item.objects.all()

    for item in menu_items:
        response = requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?s={item.title.replace(" ","_")}').json()
\
        JSON_DATA.append({
            'title': item.title,
            'price': item.price,
            'description': response['meals'][0]['strInstructions'],
            'spicy_level': item.spicy_level,
            'category': model_to_dict(Category.objects.get(id=item.category_id)),
            'cuisine': model_to_dict(Cuisine.objects.get(id=item.cuisine_id)),
            'image':response['meals'][0]['strMealThumb'],
            'video':response['meals'][0]['strYoutube']
            
        })
    if len(JSON_DATA) == 0:
        return HttpResponse('<h1>NO Response<h1>')
    else:
        return JsonResponse(JSON_DATA, safe=False)


