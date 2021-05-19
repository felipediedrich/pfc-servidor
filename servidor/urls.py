from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from iot.api import DispositivoViewSet, AgendamentoViewSet

from servidor.api import UserViewSet

# , serializers, viewsets
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r"dispositivos", DispositivoViewSet)
router.register(r"agendamento", AgendamentoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]