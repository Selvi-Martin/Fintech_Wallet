from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response  import Response
from rest_framework import status
from django.db import transaction as db_transaction
from django.shortcuts import get_object_or_404
from .models import Transaction, Wallet
from .serializers import WalletSerializer

class WalletDetailView(APIView):
    """ GET/ wallets /<id> - View balance and transaction history"""
    def get(self, request, wallet_id):
        wallet=get_object_or_404(Wallet, id= wallet_id)
        serializer = WalletSerializer(Wallet)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DepositView(APIView):
    """POST / wallets / <id>/deposit - Add money """
    def post(self, request, wallet_id):
        amount=request.data.get('amount')
        if not amount or float(amount)<0:
            return Response({"error": "Amount must be a positive number"}, status=status.HTTP_400_BAD_REQUEST)
        wallet= get_object_or_404(Wallet, id=wallet_id)
    
        with db_transaction.atomic():   # Atomic - Treats entire steps as a single unit. If one steps fail nothing is processed and the 1st processed also reverted. So no damage done on both side
            wallet.balance +=float(amount)
            wallet.save()
            Transaction.objects.create(
                wallet=wallet,
                transaction_type='DEPOSIT',
                amount=amount,
                remarks=request.data.get('remarks', '')
            )
        return Response(WalletSerializer(wallet).data, status=status.HTTP_201_CREATED)

class Withdrawaldetails(APIView):
    """ POST/ wallets / <id> / withdraw - deduct money"""
    def post(self, request,wallet_id):
        amount=request.data.get('amount')
        if not amount or float(amount)<0:
            return Response({"error": "Amount must be a positive number"}, status=status.HTTP_400_BAD_REQUEST)
        wallet=get_object_or_404(Wallet, wallet_id)

        if(wallet.balance < float(amount)):
            return Response({"error": "Insufficient Balance"}, status=status.HTTP_400_BAD_REQUEST)
        
        with db_transaction.atomic():
            wallet.balance -= float(amount)
            wallet.save()
            Transaction.objects.create (
                wallet=wallet,
                transaction_type="WITHDRAW",
                amount=amount,
                remarks=request.data.get('remarks', '')
            )
        return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)

            



