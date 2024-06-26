# Generated by Django 4.0.4 on 2024-03-12 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_product_description_alter_product_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_after_discount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='leave blank if discount not applicable ', max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_code',
            field=models.SlugField(blank=True, help_text='automatically populates with unique slug (not required)', unique=True),
        ),
    ]
