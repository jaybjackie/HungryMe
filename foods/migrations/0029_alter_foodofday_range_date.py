# Generated by Django 4.1.1 on 2022-11-12 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0028_alter_foodofday_range_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodofday",
            name="range_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 13, 19, 14, 31, 570757, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date end",
            ),
        ),
    ]