# Generated by Django 4.2.7 on 2024-06-16 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_rename_product_id_wishlistitem_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_id',
            new_name='product',
        ),
    ]