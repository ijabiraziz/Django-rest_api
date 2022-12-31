from django.contrib import admin
from .models import Stock, InsiderTransactions, Valuation

# Register your models here.

class InsiderTransactionsAdmin(admin.ModelAdmin):
    list_per_page = 10


class StockAdmin(admin.ModelAdmin):
    list_per_page = 10
    
    
    
admin.site.register(InsiderTransactions, InsiderTransactionsAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Valuation)
