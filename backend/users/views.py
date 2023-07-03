from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets
from users.serializers import UserModelSerializer

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer



