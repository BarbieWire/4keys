# Generated by Django 4.0.4 on 2024-03-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_rename_productpictures_productpicture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(help_text='unlimited text length'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(help_text='up to 500 symbols', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='normal_price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_after_discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=12.99, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='vendor_code',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
