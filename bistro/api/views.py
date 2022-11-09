from django.shortcuts import render
from django.http import JsonResponse
from api.models import Menu_item, Category, Cuisine
from pprint import pprint as pp

# Create your views here.


def getData(request):
    if request.method == 'GET':

        category = Category.objects.values()
        cuisine = Cuisine.objects.values()
        menu_item = Menu_item.objects.values()





        return JsonResponse({'data': data})






        
        # data = {
        #     'title':list(menu_item)[1]['title'],
        #     'price':list(menu_item)[1]['price'],
        #     'cuisine': list(cuisine.filter(id = 1)),
        #     'category': list(category.filter(id = 2)),
        #     'spicy_level':list(menu_item)[1]['spicy_level'],
      
        # }