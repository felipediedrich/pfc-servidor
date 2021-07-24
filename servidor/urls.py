from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from iot.api import DispositivoViewSet, AgendamentoViewSet

from servidor.api import UserViewSet

user_router = routers.DefaultRouter()
user_router.register(r"dispositivos", DispositivoViewSet)
user_router.register(r"agendamento", AgendamentoViewSet)

admin_router = routers.DefaultRouter()
admin_router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(user_router.urls)),
    path('api/admin/', include(admin_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]