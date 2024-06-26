# Generated by Django 4.0.4 on 2024-03-03 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Product attribute',
                'verbose_name_plural': 'Product attributes',
            },
        ),
        migrations.CreateModel(
            name='ProductAttributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.productattribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.product')),
            ],
            options={
                'verbose_name': 'Product attribute value',
                'verbose_name_plural': 'Product attribute values',
            },
        ),
    ]
