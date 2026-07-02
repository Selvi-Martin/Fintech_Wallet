from rest_framework import serializers
from .models import Transaction, Wallet

class TransactionSerializer(serializers.ModelSerializer):  #modelserializer automatically generates the field then alone serializer
    model=Transaction
    fields= ['id', 'transaction_type', 'amount', 'timestamp', 'remarks']

class WalletSerializer(serializers.ModelSerializer):
    transactions= TransactionSerializer(many=True, read_only=True)  # Able to see all the transactions made in wallet
    username=serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model=Wallet
        fields=['id', 'username', 'wallet', 'transactions']