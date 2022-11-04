# Generated by Django 4.1.1 on 2022-11-02 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0014_alter_foodofday_range_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodofday",
            name="range_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 3, 7, 3, 38, 996451, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date end",
            ),
        ),
    ]