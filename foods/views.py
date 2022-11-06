from django.shortcuts import render, get_object_or_404, redirect 
from foods.get_data import api_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q, Avg
from foods.models import Menu
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from .forms import RegisterForm
from django.contrib import messages
import datetime
from foods.models import Menu ,FoodOfDay, MenuRating
import random
from time import timezone

@cache_page(60 * 60)
@vary_on_cookie
def index(request):
    search_post = request.GET.get('search')
    if search_post:
        menu_list = Menu.objects.filter(Q(menu_name__icontains=search_post) & \
            Q(description__icontains=search_post) & Q(ingredients__icontains=search_post))  
    else:
        menu_list = Menu.objects.all().order_by()[:24]

    # feed = api_response()
    # for entry in feed:
    #     try:
    #         get_menu_name = entry['display']['displayName']
    #     except:
    #         get_menu_name = 'missing menu name'

    #     try:
    #         get_difficulty = entry['content']['tags']['difficulty'][0]['display-name']
    #     except:
    #         get_difficulty = 'No information'

    #     try:
    #         get_kcal = [element['value'] for element \
    #             in entry['content']['nutrition']['nutritionEstimates'] \
    #                 if element['attribute'] == 'ENERC_KCAL'][0]
    #     except:
    #         get_kcal = -99
    #     try:
    #         get_fat = [element['value'] for element \
    #             in entry['content']['nutrition']['nutritionEstimates'] \
    #                 if element['attribute'] == 'FAT_KCAL'][0]
    #     except:
    #         get_fat = -99
    #     try:
    #         get_sugar = [element['value'] for element \
    #             in entry['content']['nutrition']['nutritionEstimates'] \
    #                 if element['attribute'] == 'SUGAR'][0]
    #     except:
    #         get_sugar = -99
    #     try:
    #         get_description = entry['seo']['web']['meta-tags']['description']
    #     except:
    #         get_description = 'No information'

    #     try:
    #         get_number_ingredients = len(entry['content']['ingredientLines'])
    #     except:
    #         get_number_ingredients = -99

    #     try:
    #         get_cooking_time = entry['content']['details']['totalTime']
    #     except:
    #         get_cooking_time = 'No information'

    #     try:
    #         get_rating = entry['content']['details']['rating']
    #     except:
    #         get_rating = 0.0

    #     try:
    #         get_picture_url = entry['display']['images'][0]
    #     except:
    #         get_picture_url = ''

    #     try:
    #         get_ingredients = entry['content']['ingredientLines']
    #     except:
    #         get_ingredients = 'No information'
            
    #     menu = Menu(
    #         menu_name= get_menu_name,
    #         creator_name = 'Official HungryMe',
    #         number_of_ingredients = get_number_ingredients,
    #         total_cooking_time = get_cooking_time,
    #         energy_kcal = get_kcal,
    #         fat_kcal = get_fat,
    #         sugar = get_sugar,
    #         picture_url = get_picture_url,
    #         rating = get_rating,
    #         difficulty = get_difficulty,
    #         description = get_description,
    #         ingredients = get_ingredients
    #     )
        # if menu not in Menu.objects.all() \
        #     and menu.menu_name != 'missing menu name'\
        #     and menu.ingredients != 'No information':
        #     menu.save()

    feeds = random.choice(Menu.objects.all())
    food_of_day  = FoodOfDay.objects.first()
    if food_of_day:
        if food_of_day.was_end():
            food_of_day.menu = feeds
            food_of_day.range_date = datetime.datetime.now() + datetime.timedelta(days=1)
            food_of_day.save()
        
    return render(request, 'foods/index.html', {"menu_list": menu_list,"food_of_day":food_of_day})
    
def detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    if MenuRating.objects.filter(menu=menu, user=request.user).first() == None:
        menu.rating = 0
    else:
        menu.rating = MenuRating.objects.filter(menu=menu, user=request.user).first().rate
    avg_rate = MenuRating.objects.filter(menu=menu).aggregate(Avg("rate"))["rate__avg"]
    return render(request, 'foods/detail.html', {"menu": menu, "avg_rate": avg_rate})

def filter(request):
    
    return render(request,'foods/filter.html',{})

def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            re_user = authenticate(username=form.cleaned_data.get('username'),
                                    password=form.cleaned_data.get('password1'))
            if user is not None:
                login(request, re_user)
            messages.success(request, "Registration successful.")
            return redirect('index')
        else:
            messages.error(request, 'Error Processing Your Request')
            return render(request, 'registration/signup.html', {'form': form})
    
    return render(request, 'registration/signup.html', {})


def rate(request, menu_id, rating):
    menu = Menu.objects.get(id=menu_id)
    MenuRating.objects.filter(menu=menu, user=request.user).delete()
    MenuRating.objects.update_or_create(user=request.user, rate=rating, menu=menu)
    return detail(request, menu_id)
