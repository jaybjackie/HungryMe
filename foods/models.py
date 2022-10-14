from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    # and more

    def __str__(self) -> str:
        return self.name