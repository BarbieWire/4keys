# Generated by Django 4.2.7 on 2024-06-01 13:34

import application.models.banner_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner',
            field=models.ImageField(upload_to=application.models.banner_models.upload_to),
        ),
    ]
