# Generated by Django 4.1.4 on 2023-01-01 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='banner',
        ),
    ]
