from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:menu_id>/', views.detail, name='detail'),
    path('signup/', views.signup, name='signup'),
    path('rate/<int:menu_id>/<int:rating>/', views.rate),
]