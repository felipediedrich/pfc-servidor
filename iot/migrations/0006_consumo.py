# Generated by Django 3.2.3 on 2021-10-06 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0005_remove_agendamento_executado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('corrente', models.FloatField()),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumo', to='iot.dispositivo')),
            ],
        ),
    ]
