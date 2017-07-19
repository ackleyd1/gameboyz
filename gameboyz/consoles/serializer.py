from rest_framework import serializers

from .models import Platform

class PlatformSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() 

    class Meta: 
        model = Platform
        fields = ['id', 'name', 'slug']