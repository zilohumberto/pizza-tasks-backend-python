# Generated by Django 3.0.5 on 2020-04-30 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0003_auto_20200430_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientbyclient',
            name='command',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='commands.Command'),
        ),
    ]