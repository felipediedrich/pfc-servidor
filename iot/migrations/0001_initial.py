# Generated by Django 3.2.3 on 2021-07-24 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('mac', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('horario', models.TimeField()),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dispositivo', to='iot.dispositivo')),
            ],
        ),
    ]
