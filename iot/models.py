from django.db import models
from django.conf import settings

class Dispositivo(models.Model):
    id = models.AutoField(primary_key=True)
    hardware_id = models.CharField(max_length=255,default="1234")
    name = models.CharField(null=False,max_length=100,default="Abajur")
    icon = models.CharField(max_length=255,default="plug.svg")
    status = models.BooleanField(default=False)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self): return self.name

class Agendamento(models.Model):
    id = models.AutoField(primary_key=True)
    dispositivo = models.ForeignKey('Dispositivo', on_delete=models.CASCADE,related_name='dispositivo')
    name = models.CharField(null=False,max_length=100)
    horario = models.TimeField()
    
    def __str__(self): return self.name