# Generated by Django 3.0.5 on 2020-05-01 02:06

import base.stores
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_auto_20200501_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=base.stores.PizzaModelStorage(), upload_to=base.stores.PizzaModelStorage.pizza_photo_path, verbose_name='photo'),
        ),
    ]