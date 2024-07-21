from django.shortcuts import render, redirect
from .models import Customer, Transactions
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from django.views import View
from .forms import FileUploadForm
from .utils import import_customers
import os
import uuid



def home(request):
    return render(request, 'core/home.html')

def customers(request):
    if request.method == "POST":
        sender_id = request.POST.get("sender_id")
        receiver_id = request.POST.get("receiver")
        amount = request.POST.get("amount")
        
        # Validate and convert sender_id
        if not sender_id or not is_valid_uuid(sender_id):
            messages.error(request, 'Invalid sender ID format.')
            return redirect('customers')
        
        # Validate and convert receiver_id
        if not receiver_id or not is_valid_uuid(receiver_id):
            messages.error(request, 'Invalid receiver ID format.')
            return redirect('customers')
        
        try:
            sender = Customer.objects.get(id=uuid.UUID(sender_id))
        except Customer.DoesNotExist:
            messages.error(request, 'Sender not found.')
            return redirect('customers')
        
        try:
            receiver = Customer.objects.get(id=uuid.UUID(receiver_id))
        except Customer.DoesNotExist:
            messages.error(request, 'Receiver not found.')
            return redirect('customers')
        
        if sender.id != receiver.id:
            try:
                amount = Decimal(amount)
            except InvalidOperation:
                messages.error(request, 'Invalid amount. Please enter a valid number.')
                return redirect('customers')
            
            if sender.balance >= amount:
                # Create a new transaction record
                transaction = Transactions.objects.create(
                    sender=sender,
                    receiver=receiver,
                    amount=amount
                )
                
                # Update sender and receiver balances
                sender.balance -= amount
                receiver.balance += amount
                
                # Save the transaction history for sender and receiver
                sender.transaction_history.add(transaction)
                receiver.transaction_history.add(transaction)
                
                # Save changes to the sender and receiver objects
                sender.save()
                receiver.save()
                
                messages.success(request, 'Transaction successful!')
            else:
                messages.error(request, 'Insufficient balance.')
        else:
            messages.error(request, "The sender and receiver are the same; it can't be done.")
        
        return redirect('customers')
    
    # For GET requests or initial page load
    customers = Customer.objects.all()
    return render(request, 'core/customers.html', {'customers': customers})

def is_valid_uuid(uuid_string):
    try:
        uuid_obj = uuid.UUID(uuid_string, version=4)
        return str(uuid_obj) == uuid_string
    except ValueError:
        return False


def transactions_history(request):
    transactions = Transactions.objects.order_by('-timestamp')

    return render(request, 'core/transactions.html', {'transactions': transactions})



class ImportCustomersView(View):
    def get(self, request):
        form = FileUploadForm()
        return render(request, 'core/import_customers.html', {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            file_name = file.name
            file_path = f'/tmp/{file_name}'  # Temporary file path

            # Save the file temporarily
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            try:
                # Import the customers
                import_customers(file_path)
                messages.success(request, 'Customers imported successfully!')
            except Exception as e:
                messages.error(request, f'Error importing customers: {str(e)}')
            finally:
                # Clean up the temporary file
                os.remove(file_path)

            return redirect('import_customers')
        else:
            messages.error(request, 'Invalid form submission.')
            return render(request, 'core/import_customers.html', {'form': form})