# Generated by Django 4.1.4 on 2023-01-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_orderitem_shipping_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='shipping_method',
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_method',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
