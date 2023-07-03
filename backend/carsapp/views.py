from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from carsapp.models import Car
from carsapp.serializers import CarModelSerializer


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer

    def get_queryset(self):
        return Car.objects.all()