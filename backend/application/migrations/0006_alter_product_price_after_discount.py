# Generated by Django 4.0.4 on 2024-03-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_product_price_after_discount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_after_discount',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='leave blank if discount not applicable', max_digits=8, null=True),
        ),
    ]
