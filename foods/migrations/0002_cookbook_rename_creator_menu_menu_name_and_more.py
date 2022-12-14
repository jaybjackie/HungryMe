# Generated by Django 4.1.1 on 2022-11-29 12:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("foods", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CookBook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
                ("cook_name", models.CharField(max_length=200)),
                (
                    "description",
                    models.CharField(
                        default="No description", max_length=250, null=True
                    ),
                ),
                ("ingredients", models.JSONField(default=None, null=True)),
                ("picture_url", models.URLField(default="")),
                ("number_of_ingredients", models.IntegerField(default=1)),
                ("energy_kcal", models.FloatField(default=0.0, null=True)),
                ("fat_kcal", models.FloatField(default=0.0, null=True)),
                ("sugar", models.FloatField(default=0.0, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="menu", old_name="creator", new_name="menu_name",
        ),
        migrations.RemoveField(model_name="menu", name="name",),
        migrations.AddField(
            model_name="menu",
            name="category",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="creator_name",
            field=models.CharField(default="Official HungryMe", max_length=50),
        ),
        migrations.AddField(
            model_name="menu",
            name="description",
            field=models.CharField(default="No description", max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="difficulty",
            field=models.CharField(default="None", max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="energy_kcal",
            field=models.IntegerField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="fat_kcal",
            field=models.IntegerField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="ingredients",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="number_of_ingredients",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="menu",
            name="nutrition",
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="picture_url",
            field=models.URLField(default="", null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="rating",
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name="menu",
            name="sugar",
            field=models.IntegerField(default=0.0, null=True),
        ),
        migrations.CreateModel(
            name="MenuRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.IntegerField(default=0)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="foods.menu"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FoodOfDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "range_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2022,
                            11,
                            30,
                            12,
                            25,
                            58,
                            387527,
                            tzinfo=datetime.timezone.utc,
                        ),
                        verbose_name="date end",
                    ),
                ),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="foods.menu"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CookbookRating",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rate", models.IntegerField(default=0)),
                (
                    "menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="foods.cookbook",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CommentCookbook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=200)),
                ("user", models.CharField(max_length=200)),
                (
                    "room_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foods.cookbook",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=200)),
                ("user", models.CharField(max_length=200)),
                (
                    "room_name",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="foods.menu",
                    ),
                ),
            ],
        ),
    ]
