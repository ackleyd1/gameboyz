import time
import datetime

from rest_framework import serializers
from .models import Game, Theme, Keyword, Franchise, Collection, EbayListing

class UnixEpochDateField(serializers.DateTimeField): 
    def to_representation(self, value): 
        """ Return epoch time for a datetime object or ``None``"""
        try: 
            return int(time.mktime(value.timetuple())) 
        except (AttributeError, TypeError): 
            return None 
    def to_internal_value(self, value): 
        return datetime.datetime.fromtimestamp(int(value)) 
        
class GameSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() 
    first_release_date = UnixEpochDateField()  

    class Meta: 
        model = Game
        fields = ['id', 'name', 'slug', 'url', 'summary', 'collections', 'franchise', 'popularity', 'total_rating', 'total_rating_count', 'first_release_date', 'keywords', 'themes', 'platforms']

class ThemeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() 

    class Meta: 
        model = Theme
        fields = ['id', 'name', 'slug']

class KeywordSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() 

    class Meta: 
        model = Keyword
        fields = ['id', 'name', 'slug']

class FranchiseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() 

    class Meta: 
        model = Franchise
        fields = ['id', 'name', 'slug']

class CollectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField() 

    class Meta: 
        model = Collection
        fields = ['id', 'name', 'slug']

class EbayListingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = EbayListing
        fields = ['title', 'game', 'country', 'location', 'url', 'condition', 'price']
