from django.urls import path
from . import views

urlpatterns = [
    path('post-data/', views.post_data, name='post_data'),
    path('<str:symbol>/', views.main_api, name='stock_list'),
    path('valuation/<str:symbol>/', views.valuation_list, name='valuation_list'),
    path('insider-transactions/<str:symbol>/', views.insider_transactions_list,
         name='insider_transactions_list'),
  
]
