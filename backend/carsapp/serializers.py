from rest_framework import serializers
from .models import Car, HistoryCar, DetailCar


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
    def validate(self, attrs):
        if attrs['brand'] == 'Toyota' and attrs['model'] == 'Mark 2':
            raise serializers.ValidationError('brand and model error')
        return attrs

class HistoryCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryCar
        fields = '__all__'
class DetailCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCar
        fields = '__all__'