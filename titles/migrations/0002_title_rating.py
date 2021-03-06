# Generated by Django 3.0.5 on 2021-05-03 16:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.SmallIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10)],
                verbose_name='Рейтинг'),
        ),
    ]
