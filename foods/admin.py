from django.contrib import admin

from .models import Menu, FoodOfDay,Comment,CookBook


admin.site.register(Menu)
admin.site.register(FoodOfDay)
admin.site.register(Comment)
admin.site.register(CookBook)

admin.site.site_header = "HungryMe Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the HungryMe Admin Area"