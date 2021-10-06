from django.db import models
from django.conf import settings
from datetime import datetime

class Dispositivo(models.Model):
    mac = models.CharField(primary_key=True,max_length=255)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=255)
    status = models.BooleanField()
    is_110 = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    last_ping = models.DateTimeField(default=datetime.now)

    def __str__(self): return self.name

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE,related_name='dispositivo')
    name = models.CharField(null=False,max_length=100)
    horario = models.TimeField()
    repetir = models.CharField(null=False,max_length=100,default="")
    modo = models.BooleanField(default=True)

    def __str__(self): return self.name

class Consumo(models.Model):
    id = models.AutoField(primary_key=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE,related_name='consumo')
    horario = models.DateTimeField(default=datetime.now)
    corrente = models.FloatField(null=False)
