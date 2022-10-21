import requests
from django.http import HttpResponse
from django.shortcuts import render

from foods.models import Menu

def index(request):
    """Fetch the data from api and display lists of menu."""
    url = "https://yummly2.p.rapidapi.com/feeds/list"

    querystring = {"limit":"25","start":"0"}

    headers = {
        "X-RapidAPI-Key": "8c2fbd63b6msh0cb0f06d6eefb0bp195126jsn7230d0695123",
        "X-RapidAPI-Host": "yummly2.p.rapidapi.com"
    }
    # get json 
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    # feed contains 23 entrys of menu
    feed = response['feed']
    for entry in feed:
        display_info = entry['display']
        content_info = entry['content']

        try:
            get_menu_name = entry['display']['displayName']
        except:
            get_menu_name = 'missing menu name'

        try:
            get_difficulty = content_info['tags']['difficulty']
        except:
            get_difficulty = 'No information'

        try:
            get_kcal = content_info['nutrition']['nutritionEstimates'][0].get('value')
        except:
            get_kcal = -99

        try:
            get_description = entry['seo']['web']['meta-tags']['description']
        except:
            get_description = 'No information'

        try:
            get_number_ingredients = len(content_info['ingredientLines'])
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
            get_picture_url = display_info['images'][0]
        except:
            get_picture_url = ''

        menu = Menu(
            menu_name= get_menu_name,
            creator_name = 'Official HungryMe',
            number_of_ingredients = get_number_ingredients,
            total_cooking_time = get_cooking_time,
            kcal = get_kcal,
            picture_url = get_picture_url,
            rating = get_rating,
            difficulty = get_difficulty,
            description = get_description
        )
        if menu not in Menu.objects.all() and menu.menu_name != 'missing menu name':
            menu.save()

    menu_list = Menu.objects.all().order_by('-id')
    return render(request, 'foods/index.html', {"menu_list": menu_list,
                                                "feed": feed})
