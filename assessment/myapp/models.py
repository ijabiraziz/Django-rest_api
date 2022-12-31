from django.db import models


# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    change = models.FloatField()

    def __str__(self):
        return self.name



class Valuation(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    market_cap = models.BigIntegerField()
    pe_ratio = models.FloatField()
    symbol = models.OneToOneField(Stock, on_delete=models.CASCADE, related_name='valuation')
    
    def __str__(self):
        return self.id



class InsiderTransactions(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=50)
    cost = models.FloatField()
    symbol = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='insider_transactions')

    def __str__(self):
        return self.name
    