# Generated by Django 4.1.4 on 2023-01-02 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_rename_cartitems_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='total',
        ),
    ]