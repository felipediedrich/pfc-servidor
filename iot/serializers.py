from rest_framework import serializers

from iot.models import Dispositivo, Agendamento


class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = [
            "hardware_id",
            "name",
            "status",
        ]

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = [
            "dispositivo__name",
            "name",
            "horario",
        ]

