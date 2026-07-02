from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) #One user uer has one one wallet and one wallet has one user. When the user is deleted, delete the respective wallet also
    balance= models.DecimalField(max_digits=12,decimal_places=2, default=0)
    created_at=models.DateTimeField(auto_now_add=True)   #Automatically adds current time when you check the balance

    def __str__(self):
        return f"{self.user.username}'s wallet - Rs{self.balance}"

class Transaction(models.Model):
    Transaction_Types=(
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
        ('TRANSFER', 'Transfer')
    )

    Wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name="Transactions")
    transaction_type=models.CharField(max_length=10, choices=Transaction_Types)
    amount=models.DecimalField(max_digits=12, decimal_places=2)
    timestamp=models.DateTimeField(auto_now_add=True)
    remarks=models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.transaction_type} of Rs{self.amount}"
