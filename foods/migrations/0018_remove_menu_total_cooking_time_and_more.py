# Generated by Django 4.1.1 on 2022-11-04 09:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0017_alter_foodofday_range_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="menu", name="total_cooking_time",),
        migrations.AlterField(
            model_name="foodofday",
            name="range_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 5, 9, 39, 43, 739934, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date end",
            ),
        ),
    ]