# Generated by Django 3.2.3 on 2021-08-02 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0003_delete_consumo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='last_ping',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
