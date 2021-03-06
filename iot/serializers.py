from rest_framework import serializers

from iot.models import Dispositivo, Agendamento

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['url','mac','name','is_110','icon','status','last_ping']

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = ['url','id','name','horario','dispositivo','repetir','modo']
