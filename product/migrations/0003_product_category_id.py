# Generated by Django 4.1.4 on 2023-01-02 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_banner'),
        ('product', '0002_remove_product_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.category'),
        ),
    ]
