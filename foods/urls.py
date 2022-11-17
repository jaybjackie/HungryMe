from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('filter/', views.filter, name='filter'),
    path('rate/<int:menu_id>/<int:rating>/', views.rate),
    path('My_cook_book/', views.cook_home, name='cook'),
    path('My_cook_book/create_menu/', views.cook_create, name='create'),
    path('My_cook_book/delete/<str:cook_name>', views.delete, name='delete')
]