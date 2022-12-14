from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg
from django import forms

        
class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    creator_name = models.CharField(max_length=50, default="Official HungryMe")
    number_of_ingredients = models.IntegerField(default=1)
    energy_kcal = models.IntegerField(default=0.0, null=True)
    fat_kcal = models.IntegerField(default=0.0, null=True)
    sugar = models.IntegerField(default=0.0, null=True)
    picture_url = models.URLField(max_length=200, default='', null=True)
    rating = models.FloatField(default=0.0, null=True)
    difficulty = models.CharField(max_length=30, default="None", null=True)
    description = models.CharField(max_length=250, default='No description', null=True)
    ingredients = models.JSONField(null=True, default=None)
    nutrition = models.JSONField(null=True, default=None)
    category = models.JSONField(null=True, default=None)

    def __str__(self) -> str:
        return f"{self.menu_name} by {self.creator_name}"

    @property
    def avg_menurating(self) -> float:
        return self.menurating_set.aggregate(Avg('rate'))['rate__avg']
        
class FoodOfDay(models.Model):
    range_date = models.DateTimeField('date end', default = timezone.now() + datetime.timedelta(days=1))
    menu = models.ForeignKey(Menu, on_delete = models.DO_NOTHING)

    def was_end(self):
        now = timezone.now()
        return self.range_date >= now

class MenuRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    menu = models.ForeignKey(Menu, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.menu.menu_name} Rating: {self.rate}"
        
class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    room_name = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

class CookBook(models.Model):
    pub_date = models.DateTimeField('date published')
    cook_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='No description', null=True)
    ingredients = models.JSONField(null=True, default=None)
    picture_url = models.URLField(max_length=200, default='', null=False)
    number_of_ingredients = models.IntegerField(default=1)
    energy_kcal = models.FloatField(default=0.0, null=True)
    fat_kcal = models.FloatField(default=0.0, null=True)
    sugar = models.FloatField(default=0.0, null=True)
    rating = models.FloatField(default=0.0, null=True)

    # difficulty = models.CharField(max_length=30, default="None", null=True)

    def __str__(self):
        return self.cook_name
    
class CommentCookbook(models.Model):
    text = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    room_name = models.ForeignKey(CookBook, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
    
class CookbookRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    menu = models.ForeignKey(CookBook, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.menu.cook_name} Rating: {self.rate}"

class Filter(models.Model):
    food_allergies = forms.MultipleChoiceField()
