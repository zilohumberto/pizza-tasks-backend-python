# Generated by Django 3.0.5 on 2020-04-28 15:39

from django.db import migrations


def load_data(apps, schema_editor):
    obj_order_status = apps.get_model("orders", "OrderStatus")
    status = [
        {
            'name': 'created',
            'description': 'created'
        },
        {
            'name': 'preparing_order',
            'description': 'preparing_order'
        },
        {
            'name': 'to_delivery',
            'description': 'Finish the cook and now can be delivery'
        },
        {
            'name': 'delivered',
            'description': 'delivered'
        },
        {
            'name': 'canceled_by_client',
            'description': 'canceled_by_client'
        },
        {
            'name': 'canceled_by_us',
            'description': 'canceled_by_us'
        },
    ]
    for element in status:
        obj_order_status(**element).save()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
