from rest_framework import serializers
from .models import Stock, Valuation, InsiderTransactions


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class ValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = '__all__'
        
        
class InsiderTransactionsSerializer(serializers.ModelSerializer):
    # symbol = serializers.PrimaryKeyRelatedField(queryset=Stock.objects.all())

    class Meta:
        model = InsiderTransactions
        fields = '__all__'