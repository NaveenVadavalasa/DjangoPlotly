from rest_framework import serializers
from .models import Daily

class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model=Daily
        fields = '__all__'