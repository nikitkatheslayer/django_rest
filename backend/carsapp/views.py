from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets

from carsapp.models import Car, HistoryCar, DetailCar
from carsapp.serializers import CarModelSerializer, HistoryCarModelSerializer, DetailCarModelSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer

class HistoryCarViewSet(viewsets.ModelViewSet):
    queryset = HistoryCar.objects.all()
    serializer_class = HistoryCarModelSerializer

class DetailCarViewSet(viewsets.ModelViewSet):
    queryset = DetailCar.objects.all()
    serializer_class = DetailCarModelSerializer

