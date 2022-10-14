from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('foods.urls')),
    path('foods/', include('foods.urls')),
    path('admin/', admin.site.urls),
]