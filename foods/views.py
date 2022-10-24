import requests
from django.shortcuts import render, get_object_or_404
from foods.get_data import api_response

from foods.models import Menu

def index(request):
    feed = api_response()
    for entry in feed:

        try:
            get_menu_name = entry['display']['displayName']
        except:
            get_menu_name = 'missing menu name'

        try:
            get_difficulty = entry['content']['tags']['difficulty'][0]['display-name']
        except:
            get_difficulty = 'No information'

        try:
            get_kcal = entry['content']['nutrition']['nutritionEstimates'][0].get('value')
        except:
            get_kcal = -99

        try:
            get_description = entry['seo']['web']['meta-tags']['description']
        except:
            get_description = 'No information'

        try:
            get_number_ingredients = len(entry['content']['ingredientLines'])
        except:
            get_number_ingredients = -99

        try:
            get_cooking_time = entry['content']['details']['totalTime']
        except:
            get_cooking_time = 'No information'

        try:
            get_rating = entry['content']['details']['rating']
        except:
            get_rating = 0.0

        try:
            get_picture_url = entry['display']['images'][0]
        except:
            get_picture_url = ''

        try:
            get_ingredients = entry['content']['ingredientLines']
        except:
            get_ingredients = 'No information'

        try:
            get_nutrition = entry['content']['nutrition']
        except:
            get_nutrition = 'No information'
            
        menu = Menu(
            menu_name= get_menu_name,
            creator_name = 'Official HungryMe',
            number_of_ingredients = get_number_ingredients,
            total_cooking_time = get_cooking_time,
            energy_kcal = get_kcal,
            picture_url = get_picture_url,
            rating = get_rating,
            difficulty = get_difficulty,
            description = get_description,
            ingredients = get_ingredients,
            nutrition = get_nutrition
        )
        if menu not in Menu.objects.all() \
            and menu.menu_name != 'missing menu name'\
            and menu.ingredients != 'No information':
            menu.save()

    menu_list = Menu.objects.all().order_by('-id')[:24]
    return render(request, 'foods/index.html', {"menu_list": menu_list,
                                                "feed": feed})

def detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'foods/detail.html', {"menu": menu})