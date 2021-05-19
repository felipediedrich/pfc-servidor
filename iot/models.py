from django.db import models
from django.conf import settings

class Dispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    hardware_id = models.CharField(max_length=255)
    name = models.CharField(null=False,max_length=100)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE,related_name='datacollector')
    name = models.CharField(null=False,max_length=100)
    horario = models.TimeField()

# class Dias(models.Model):
#     id = models.AutoField(primary_key=True)
#     dia = models.CharField(max_length=1,choices=((0,'Domingo'),(1,'Segunda'),(2,'Terça'),(3,'Quarta'),(4,'Quinta'),(5,'Sexta'),(6,'Sabado')))
