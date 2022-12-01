# Generated by Django 4.1.1 on 2022-11-30 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0005_cookbook_rating_alter_foodofday_range_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Filter",
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
            ],
        ),
        migrations.AlterField(
            model_name="foodofday",
            name="range_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 12, 1, 8, 41, 21, 278566, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date end",
            ),
        ),
    ]