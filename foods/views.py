from re import search
from time import timezone
from django.shortcuts import render, get_object_or_404, redirect 
from foods.get_data import api_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
import datetime
from foods.models import Menu ,FoodOfDay
import random


def index(request):
    feed = api_response()
    search_post = request.GET.get('search')
    feeds = random.choice(Menu.objects.all())
    if search_post:
        menu_list = Menu.objects.filter(Q(menu_name__icontains=search_post) & \
            Q(description__icontains=search_post) & Q(ingredients__icontains=search_post))
    else:
        menu_list = Menu.objects.all().order_by('-id')[:24]
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
            get_kcal = [element['value'] for element \
                in entry['content']['nutrition']['nutritionEstimates'] \
                    if element['attribute'] == 'ENERC_KCAL'][0]
        except:
            get_kcal = -99
        try:
            get_fat = [element['value'] for element \
                in entry['content']['nutrition']['nutritionEstimates'] \
                    if element['attribute'] == 'FAT_KCAL'][0]
        except:
            get_fat = -99
        try:
            get_sugar = [element['value'] for element \
                in entry['content']['nutrition']['nutritionEstimates'] \
                    if element['attribute'] == 'SUGAR'][0]
        except:
            get_sugar = -99
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
            
        menu = Menu(
            menu_name= get_menu_name,
            creator_name = 'Official HungryMe',
            number_of_ingredients = get_number_ingredients,
            total_cooking_time = get_cooking_time,
            energy_kcal = get_kcal,
            fat_kcal = get_fat,
            sugar = get_sugar,
            picture_url = get_picture_url,
            rating = get_rating,
            difficulty = get_difficulty,
            description = get_description,
            ingredients = get_ingredients
        )
        if menu not in Menu.objects.all() \
            and menu.menu_name != 'missing menu name'\
            and menu.ingredients != 'No information':
            menu.save()

    food_of_day  = FoodOfDay.objects.first()
    if food_of_day.was_end():
        food_of_day.menu = feeds
        food_of_day.range_date = timezone.now() +  datetime.timedelta(days=1)
        food_of_day.save()
        
    # return render(request, 'foods/index.html', {"menu_list": menu_list,
    #                                             "feed": feed})
    return render(request, 'foods/index.html', {"menu_list": menu_list,"food_of_day":food_of_day})

    
def detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'foods/detail.html', {"menu": menu})

def search_bar(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        menus = Menu.objects.filter(menu_name__contains = searched)
        return render(request, 
        'foods/search_bar.html',
        {'searched':searched,
        'menu' : menus})
    else:
        return render(request, 
        'foods/search_bar.html',
        {})

def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('foods:index')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

