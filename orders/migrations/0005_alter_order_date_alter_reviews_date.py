# Generated by Django 4.0 on 2022-01-12 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_date_alter_reviews_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 12, 20, 49, 22, 65834)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 12, 20, 49, 22, 66836)),
        ),
    ]
