from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Car


class CarModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
