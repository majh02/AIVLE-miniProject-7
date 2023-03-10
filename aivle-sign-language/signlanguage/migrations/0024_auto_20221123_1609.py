# Generated by Django 3.2 on 2022-11-23 07:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signlanguage', '0023_alter_aimodel_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('searchkey', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='aimodel',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 16, 9, 9, 675836), verbose_name='date published'),
        ),
    ]
