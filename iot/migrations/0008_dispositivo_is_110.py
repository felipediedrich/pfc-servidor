# Generated by Django 3.2.3 on 2021-10-06 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0007_consumo_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='is_110',
            field=models.BooleanField(default=True),
        ),
    ]
