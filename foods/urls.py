from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.detail, name='detail'),
    path('filter/', views.filter, name='filter'),
    path('filter/result/', views.filter_result, name='result'),
    path('rate/<int:menu_id>/<int:rating>/', views.rate),
    path('My_cook_book/', views.cook_home, name='cook'),
    path('My_cook_book/<str:cook_name>', views.show_food, name='show_food'),
    path('My_cook_book/create_menu/', views.cook_create, name='create'),
    path('top-rated-foods/', views.top_rate_foods, name='top-rated'),
    path('My_cook_book/delete/<str:cook_name>', views.delete, name='delete'),
]