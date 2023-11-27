# serializers.py in your Django app

from rest_framework import serializers
from .models import House, Facilities

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('name', 'latitude', 'longitude')

class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ('name', 'latitude', 'longitude')
