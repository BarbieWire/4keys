# Generated by Django 4.0.4 on 2024-03-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_usermodified_profile_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodified',
            name='username',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
    ]
