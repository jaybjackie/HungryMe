from django.db import models


class Menu(models.Model):
    menu_name = models.CharField(max_length=50)
    creator_name = models.CharField(max_length=50, default="Official HungryMe")
    number_of_ingredients = models.IntegerField(default=1)
    total_cooking_time = models.CharField(max_length=25, default='15 minutes', null=True)
    energy_kcal = models.FloatField(default=0.0, null=True)
    picture_url = models.URLField(max_length=200, default='', null=True)
    rating = models.FloatField(default=0.0, null=True)
    difficulty = models.CharField(max_length=30, default="None", null=True)
    description = models.CharField(max_length=250, default='No description', null=True)
    ingredients = models.TextField(max_length=None, null=True)
    nutrition = models.TextField(max_length=None, null=True)

    def __str__(self) -> str:
        return f"{self.menu_name} by {self.creator_name}"