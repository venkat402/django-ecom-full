# Generated by Django 4.1.4 on 2023-01-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_category'),
        ('cart', '0005_rename_discount_cartitems_quantity_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItems',
            new_name='CartItem',
        ),
    ]
