# Generated by Django 4.0 on 2022-01-13 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_remove_payment_transaction_id_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 13, 40, 7, 607705)),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 13, 13, 40, 7, 608705)),
        ),
    ]
