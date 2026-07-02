from django.urls import path  #defines url path
from .views import WalletDetailView, Withdrawaldetails, DepositView

urlpatterns=[
    path('wallets/<int:wallet_id>/', WalletDetailView.as_view(), name= 'wallet-detail'),
    path('wallets/<int:wallet_id>/deposit', DepositView.as_view(), name='wallet-deposit'),
    path('wallets/<int:wallet_id>/withdraw', Withdrawaldetails.as_view(), name='wallet-withdraw')
]