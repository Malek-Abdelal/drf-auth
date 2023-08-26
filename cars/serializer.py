from rest_framework import serializers
from .models import Car
class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['owner', 'company', 'model', 'year_of_production', 'color']