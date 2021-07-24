from rest_framework import viewsets
from iot.models import Dispositivo, Agendamento
from iot.serializers import DispositivoSerializer, AgendamentoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response

class IsOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsDispositivoOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        return obj.dispositivo.owner == request.user

class DispositivoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsOwner]
    serializer_class = DispositivoSerializer
    queryset = Dispositivo.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(owner=self.request.user) 
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AgendamentoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsDispositivoOwner]
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(dispositivo__owner=self.request.user) 
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
