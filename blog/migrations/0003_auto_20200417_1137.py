# Generated by Django 3.0.5 on 2020-04-17 05:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200416_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateField(default=datetime.datetime(2020, 4, 17, 5, 37, 39, 414863, tzinfo=utc)),
        ),
    ]
