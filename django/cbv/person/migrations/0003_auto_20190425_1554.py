# Generated by Django 2.1.8 on 2019-04-25 06:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20190425_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name=django.core.validators.MinValueValidator(20, message='미성년자 논노!')),
        ),
    ]
