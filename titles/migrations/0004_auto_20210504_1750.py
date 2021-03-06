# Generated by Django 3.0.5 on 2021-05-04 14:50

from django.db import migrations, models

import titles.validators


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0003_remove_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True, validators=[titles.validators.year_validator]),
        ),
    ]
