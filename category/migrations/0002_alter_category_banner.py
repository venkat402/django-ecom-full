# Generated by Django 4.1.4 on 2023-01-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='banner',
            field=models.ImageField(blank=True, default='no_image/banner-no-image.jpeg', null=True, upload_to='categories/'),
        ),
    ]
