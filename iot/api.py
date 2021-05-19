from rest_framework import viewsets
from iot.models import Dispositivo, Agendamento
from iot.serializers import DispositivoSerializer, AgendamentoSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
