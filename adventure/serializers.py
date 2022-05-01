from rest_framework import serializers

from adventure import models


class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = '__all__'


class ServiceAreaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceArea
        fields = '__all__'
