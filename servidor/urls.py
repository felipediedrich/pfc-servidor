from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from iot.api import DispositivoViewSet, AgendamentoViewSet
from servidor.api import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r"dispositivos", DispositivoViewSet)
router.register(r"agendamento", AgendamentoViewSet)
router.register(r"agendamento", AgendamentoViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]