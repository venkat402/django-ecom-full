# Generated by Django 4.1.4 on 2023-01-02 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_remove_cartitem_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cart'),
        ),
    ]