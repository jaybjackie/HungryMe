# Generated by Django 3.2.7 on 2022-10-25 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20221025_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='nutrition',
        ),
    ]