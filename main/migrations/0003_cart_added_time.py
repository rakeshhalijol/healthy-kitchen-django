# Generated by Django 3.2.7 on 2021-10-07 17:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='added_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 7, 17, 40, 58, 623048, tzinfo=utc)),
        ),
    ]
