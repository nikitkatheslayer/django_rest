from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Car


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.save()

        return instance