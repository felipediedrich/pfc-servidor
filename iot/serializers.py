from rest_framework import serializers

from iot.models import Dispositivo, Agendamento

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ['url','mac','name','icon','status']

class AgendamentoSerializer(serializers.ModelSerializer):
    dispositivo_name = serializers.CharField(source='dispositivo.name')

    class Meta:
        model = Agendamento
        fields = ['url','id','name','horario','dispositivo_name']
