# Generated by Django 2.1.7 on 2019-02-24 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190224_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user_rating',
            field=models.FloatField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
