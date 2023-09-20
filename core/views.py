from django.shortcuts import render, redirect
from .models import Customer, Transactions
from django.contrib import messages
from decimal import Decimal


def home(request):
    return render(request, 'core/home.html')

def customers(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        sender_name = request.POST.get("sender")
        receiver_id = request.POST.get("receiver")
        amount = request.POST.get("amount")

        # Access the "sender" value and split it into first and last names
        sender_first_name, sender_last_name = sender_name.split(" ")

        # Query the database to find the customer with matching names (sender)
        customers_with_matching_names = Customer.objects.filter(
            first_name=sender_first_name,
            last_name=sender_last_name
        )
        if customers_with_matching_names.exists():
            # Get the first customer with matching names
            customer = customers_with_matching_names.first()

            # Retrieve the customer's ID
            sender_id = customer.id
            
        else:
            # Handle the case where the customer is not found
            sender_id = None

        sender = Customer.objects.get(id=sender_id)
        receiver = Customer.objects.get(id=receiver_id)
        
        if sender_id != int(receiver_id):
            if sender.balance >= float(amount):
                # Create a new transaction record
                transaction = Transactions.objects.create(
                    sender=sender,
                    receiver=receiver,
                    amount=amount
                )
                
                # Update sender and receiver balances
                sender.balance -= Decimal(amount)
                receiver.balance += Decimal(amount)

                # Save the transaction history for sender and receiver
                sender.transaction_history.add(transaction)
                receiver.transaction_history.add(transaction)

                # Save changes to the sender and receiver objects
                sender.save()
                receiver.save()
                messages.success(request, 'Transaction successful!')
                return redirect('customers')

            else:
                messages.error(request, 'Insufficient balance.')
                return redirect('customers')

        else:
                messages.error(request, "The sender and receiver are the same; it can't be done.")
                return redirect('customers')

    return render(request, 'core/customers.html', {'customers': customers})


def transactions_history(request):
    transactions = Transactions.objects.order_by('-timestamp')

    return render(request, 'core/transactions.html', {'transactions': transactions})