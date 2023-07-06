from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from todoapp.models import projectModel, todoModel
from todoapp.serializers import projectSerializer, todoSerializer


class projectViewSet(ModelViewSet):
    queryset = projectModel.objects.all()
    serializer_class = projectSerializer

class todoViewSet(ModelViewSet):
    queryset = todoModel.objects.all()
    serializer_class = todoSerializer