# Generated by Django 3.2.11 on 2023-08-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blogmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
