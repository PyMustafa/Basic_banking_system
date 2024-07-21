from django.db import models
import uuid

# Create your models here.
from django.db import models

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    transaction_history = models.ManyToManyField('Transactions', related_name='related_customers', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Transactions(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sent_transactions')
    receiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='received_transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction from {self.sender} to {self.receiver}"