# Generated by Django 4.0.4 on 2024-03-04 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_productattribute_productattributevalue'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductPictures',
            new_name='ProductPicture',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='normal_price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='discount',
            new_name='price_after_discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='main_image',
        ),
    ]
