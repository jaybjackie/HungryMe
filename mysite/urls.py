from django.contrib import admin
from django.urls import include, path
from foods import views

urlpatterns = [
    path('', include('foods.urls')),
    path('foods/', include('foods.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]