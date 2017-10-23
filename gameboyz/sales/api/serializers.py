from django.apps import apps
from rest_framework import serializers

GameSale = apps.get_model('sales', 'GameSale')
ConsoleSale = apps.get_model('sales', 'ConsoleSale')

class SaleSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameSale
        fields = ['price', 'country', 'location', 'condition', 'sold']

class GameSaleSerializer(serializers.ModelSerializer):
    game = serializers.StringRelatedField()

    class Meta:
        model = GameSale
        fields = ['game', 'price', 'country', 'location', 'condition', 'sold']

class ConsoleSaleSerializer(serializers.ModelSerializer):
    console = serializers.StringRelatedField()

    class Meta:
        model = ConsoleSale
        fields = ['console', 'price', 'country', 'location', 'condition', 'sold']