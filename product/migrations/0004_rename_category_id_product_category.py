# Generated by Django 4.1.4 on 2023-01-02 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
    ]
