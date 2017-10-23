from itertools import chain

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from .serializers import SaleSerializer, GameSaleSerializer, ConsoleSaleSerializer
from gameboyz.sales.models import GameSale, ConsoleSale

class SaleListView(APIView):
    def get(self, request, format=None):
        sales = list(chain(GameSale.objects.all(), ConsoleSale.objects.all()))
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

class GameSaleListView(ListAPIView):
    serializer_class = GameSaleSerializer
    model = GameSale
    queryset = GameSale.objects.all().order_by('-price')[:10]

class ConsoleSaleListView(ListAPIView):
    serializer_class = ConsoleSaleSerializer
    model = ConsoleSale
    queryset = ConsoleSale.objects.all().order_by('-price')[:10]


