# Generated by Django 2.1.7 on 2019-02-24 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190224_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release_date',
            new_name='release_year',
        ),
    ]
