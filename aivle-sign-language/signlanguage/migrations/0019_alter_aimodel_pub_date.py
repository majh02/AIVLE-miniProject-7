# Generated by Django 3.2 on 2022-11-23 06:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0018_alter_aimodel_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aimodel',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 15, 23, 57, 473372), verbose_name='date published'),
        ),
    ]
