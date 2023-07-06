from rest_framework import serializers
from .models import projectModel, todoModel

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectModel
        fields = '__all__'

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoModel
        fields = '__all__'
