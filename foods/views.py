from django.shortcuts import render, get_object_or_404, redirect 
from foods.get_data import api_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.db.models import Q, Avg
from foods.models import CookBook, Menu
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from .forms import RegisterForm
from django.contrib import messages
import datetime
from foods.models import Menu ,FoodOfDay, MenuRating,CookBook,Comment
import random
# from time import timezone
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# from .forms import CommentFrom


@cache_page(60 * 60)
@vary_on_cookie
def index(request):
    search_post = request.GET.get('search')
    if search_post:
        menu_list = Menu.objects.filter(Q(menu_name__icontains=search_post) & \
            Q(description__icontains=search_post) & Q(ingredients__icontains=search_post))
    else:
        menu_list = Menu.objects.all().order_by()[:24]

    # Fetch data from api
    # feed = api_response()
    # save_menu(feed)

    feeds = random.choice(Menu.objects.all())
    food_of_day  = FoodOfDay.objects.first()
    if food_of_day:
        if food_of_day.was_end():
            food_of_day.menu = feeds
            food_of_day.range_date = datetime.datetime.now() + datetime.timedelta(days=1)
            food_of_day.save()
        
    return render(request, 'foods/index.html', {"menu_list": menu_list,"food_of_day":food_of_day})

def save_menu(feed):
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
            get_nutrition = entry['content']['tags']['nutrition']["display-name"]
        except:
            get_nutrition = 'No information'
        
        try:
            get_category = entry['content']['ingredientLines'][0]
        except:
            get_category = 'No information'
            
        menu = Menu(
            menu_name= get_menu_name,
            creator_name = 'Official HungryMe',
            number_of_ingredients = get_number_ingredients,
            energy_kcal = get_kcal,
            fat_kcal = get_fat,
            sugar = get_sugar,
            picture_url = get_picture_url,
            rating = get_rating,
            difficulty = get_difficulty,
            description = get_description,
            ingredients = get_ingredients,
            nutrition = get_nutrition,
            category = get_category
        )
        if get_menu_name != 'missing menu name'\
            and get_ingredients != 'No information'\
            and get_picture_url != '':
            if not Menu.objects.filter(menu_name= menu.menu_name).exists():
                menu.save()
    
def detail(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    if request.user.is_authenticated:
        if MenuRating.objects.filter(menu=menu, user=request.user).first() == None:
            menu.rating = 0
        else:
            menu.rating = MenuRating.objects.filter(menu=menu, user=request.user).first().rate
    else:
        menu.rating = 0
    avg_rate = MenuRating.objects.filter(menu=menu).aggregate(Avg("rate"))["rate__avg"]
    comment_object = Comment.objects.filter(room_name = menu)
    user = request.user

    if request.method == 'POST':
        comment_text = request.POST.get("newtext")
        print(comment_text)
        comment = Comment(text = comment_text, user = user, room_name = menu)
        comment.save()
        return redirect("index")
    else:
        return render(request, 'foods/detail.html', {"menu": menu, "avg_rate": avg_rate,"comment_object": comment_object,})

def filter(request):
    allergies_food = [{"name" : "wheat", "icon": "fa-solid fa-wheat-awn"}, {"name" :"diary", "icon": "fa-solid fa-glass-water"},{"name" :"peanut","icon": "fa-regular fa-lemon"}, 
    {"name" :"egg","icon": "fa-solid fa-egg"}, {"name":"seafood", "icon" : "fa-solid fa-shrimp"}]
    decision_food =[{},{},{}]
    print("################################################################")
    if request.method == 'POST':
        comment_text = request.POST.get("allergie")
        print (comment_text)
        
    # feed = api_response()
    # for entry in feed:
    #     try:
    #         get_menu_name = entry['display']['displayName']
    #     except:
    #         get_menu_name = 'missing menu name'

    #     try:
    #         get_picture_url = entry['display']['images'][0]
    #     except:
    #         get_picture_url = ''
        
    #     try:
    #         get_nutrition = entry['content']['tags']['nutrition']["display-name"]
    #     except:
    #         get_nutrition = 'No information'
        
    #     try:
    #         get_category = entry['content']['ingredientLines'][0]
    #     except:
    #         get_category = 'No information'
        
    #     try:
    #         get_ingredients = entry['content']['ingredientLines']
    #     except:
    #         get_ingredients = 'No information'

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

    #     menu = Menu(
    #         menu_name= get_menu_name,
    #         energy_kcal = get_kcal,
    #         fat_kcal = get_fat,
    #         sugar = get_sugar,
    #         picture_url = get_picture_url,
    #         ingredients = get_ingredients,
    #         nutrition = get_nutrition,
    #         category = get_category
    #     )
    #     if not Menu.objects.filter(menu_name= menu.menu_name).exists():
    #         menu.save()
    
    return render(request,'foods/filter.html', {"allergies":allergies_food})

def filter_result(request):
    if request.method == 'POST':
        print(request.POST)
        val = dict(request.POST)
        print("##########################################")
        print(val['allergie'])
        filter_menu_list = []
        menu_list = Menu.objects.all().order_by()[:24]
        for menu in menu_list:
            if menu.ingredients not in val['allergie']:
                filter_menu_list.append(menu)

        # not_allergie = Menu.objects.filter(ingredients=val['allergie']).exclude(True)
        # print (not_allergie)

    # Fetch data from api
    # feed = api_response()
    # save_menu(feed)

    feeds = random.choice(Menu.objects.all())

    return render(request, 'foods/filter_result.html', {"filter_menu_list": filter_menu_list})
        # call filter method

    return render(request, 'foods/filter_result.html', {
        # filtered value
        "filter_menu_list": [
            {
                "id": 1,
                "menu_name": 'mock menu name',
                "picture_url": 'mock picture_url',
                "avg_menurating": 4
            }
        ]
    })

def signup(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            print (user)
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


@login_required
def rate(request, menu_id, rating):
    menu = Menu.objects.get(id=menu_id)
    MenuRating.objects.filter(menu=menu, user=request.user).delete()
    MenuRating.objects.update_or_create(user=request.user, rate=rating, menu=menu)
    return detail(request, menu_id)


@login_required
def review(request, menu_id, reviewing):
    menu = Menu.objects.get(id=menu_id)
    Comment.objects.filter(menu=menu, user=request.user).delete()
    Comment.objects.update_or_create(user=request.user, review=reviewing, menu=menu)
    return detail(request, menu_id)

    
@login_required
def cook_home(request):
    cook_book = CookBook.objects.all()
    context = {
        'cook_book': cook_book,
    }
    return render(request, '../templates/foods/cookhome.html', context)


@login_required
def cook_create(request):
    user = request.user
    if request.method == "POST":
        name = request.POST.get("title")
        des = request.POST.get("description")
        Ing = request.POST.get("Ingredients")
        totalcal = request.POST.get("totalcalories")
        fatcal = request.POST.get("fatcalories")
        sugargrams = request.POST.get("sugargrams")
        file = request.POST.get("upfile")
        create = CookBook(
                            pub_date=timezone.now(),
                            cook_name=name,
                            user=request.user,
                            description=des,
                            ingredients=Ing,
                            energy_kcal=totalcal,
                            fat_kcal=fatcal,
                            sugar=sugargrams,
                            picture_url=file,
                            )
        create.save()
        return redirect("/My_cook_book")
    context = {}
    return render(request, '../templates/foods/createmenu.html', context)

def top_rate_foods(request):
    menu_list = Menu.objects.all()
    rated_menu = [Menu.objects.get(pk=menu.id) for menu in menu_list if Menu.objects.get(pk=menu.id).avg_menurating != None][:10]
    sort_rated = sorted(rated_menu, key=lambda menu: menu.avg_menurating, reverse=True)
    
    return render(request, 'foods/top_foods.html', {"rated_chart": sort_rated})

def delete(request,cook_name):
    member = CookBook.objects.get(cook_name=cook_name)
    member.delete()
    return redirect("/My_cook_book/")

def community(request):
    feed = api_response()
    for entry in feed:
        pass
    
    context = {}
    return render(request, '../templates/foods/community.html', context)
