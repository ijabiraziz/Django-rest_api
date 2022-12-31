from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializers import StockSerializer, ValuationSerializer, InsiderTransactionsSerializer
from .models import Stock, Valuation,InsiderTransactions
from django.db.models import Avg


@api_view(['GET'])
def main_api(request, symbol):
    stock = Stock.objects.get(symbol=symbol)
    insider_transactions = InsiderTransactions.objects.filter(symbol=symbol)[:10]
    valuation = Valuation.objects.get(symbol=symbol)

    stock_serializer = StockSerializer(stock)
    insider_transactions_serializer = InsiderTransactionsSerializer(insider_transactions, many=True)
    valuation_serializer = ValuationSerializer(valuation)

    data = {
        'stock': stock_serializer.data,
        'insider_transactions': insider_transactions_serializer.data,
        'valuation': valuation_serializer.data,
    }
    return Response(data)



@api_view(['GET'])
def valuation_list(request, symbol):
    valuation = Valuation.objects.get(symbol=symbol)
    stock = Stock.objects.get(symbol=symbol)
    serializer = ValuationSerializer(valuation)
    data = {
        'valuation': serializer.data,
        'market_cap_per_share': valuation.market_cap / stock.price,
    }
    return Response(data)



@api_view(['GET'])
def insider_transactions_list(request, symbol):
    cost = request.GET.get('cost')
    
    print(cost)
    if cost is not None:
        insider_transactions = InsiderTransactions.objects.filter(symbol=symbol, cost__gte=cost)
        
    else:
        insider_transactions = InsiderTransactions.objects.filter(symbol=symbol)
        
    serializer = InsiderTransactionsSerializer(insider_transactions, many=True)
    data = {
        'insider_transactions': serializer.data,
        'average_cost': insider_transactions.aggregate(Avg('cost'))['cost__avg'],
    }
    return Response(data)



@api_view(['POST'])
@permission_classes([AllowAny])
def post_data(request):
    # Validate and save the data in the Stock model
    stock_data = request.data['stock']
    stock_data_s = request.data['stock'].get('symbol')
    
    stock_serializer = StockSerializer(data=stock_data)
    if stock_serializer.is_valid():
        stock_serializer.save()
    else:
        return Response(stock_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Validate and save the data in the InsiderTransactions model
    insider_transactions_data = request.data['insider_transactions']
    print(stock_data_s)
    for transaction in insider_transactions_data:
        transaction['symbol'] = stock_data_s
    insider_transactions_serializer = InsiderTransactionsSerializer(data=insider_transactions_data, many=True)
    if insider_transactions_serializer.is_valid():
        insider_transactions_serializer.save()
    else:
        return Response(insider_transactions_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    data ={'message':"data is successfully saved",'saved_data':{        
        'stock':stock_serializer.data,
        'insider_tranisctions':insider_transactions_serializer.data         
    }}

    return Response(data=data,status=status.HTTP_201_CREATED)
