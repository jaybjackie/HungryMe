from django.contrib import admin
from django.urls import include, path
from foods import views

from django.views.generic import RedirectView
urlpatterns = [
    path('', include('foods.urls')),
    path('foods/', RedirectView.as_view(url="/")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
]