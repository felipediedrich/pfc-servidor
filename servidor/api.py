from rest_framework import viewsets
from django.contrib.auth.models import User
from servidor.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
