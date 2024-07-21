from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from decimal import Decimal
import uuid

from .models import Customer

class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            first_name="Mustafa",
            last_name="Said",
            email="Mustafa@example.com",
            balance=Decimal('1000.00')
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.first_name, "Mustafa")
        self.assertEqual(self.customer.last_name, "Said")
        self.assertEqual(self.customer.email, "Mustafa@example.com")
        self.assertEqual(self.customer.balance, Decimal('1000.00'))

    def test_customer_str_representation(self):
        self.assertEqual(str(self.customer), "Mustafa Said")

class CustomersViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.customer1 = Customer.objects.create(
            first_name="Mustafa",
            last_name="Said",
            email="Mustafa@example.com",
            balance=Decimal('1000.00')
        )
        self.customer2 = Customer.objects.create(
            first_name="Sarah",
            last_name="samy",
            email="Sarah@example.com",
            balance=Decimal('500.00')
        )

    def test_customers_view_GET(self):
        response = self.client.get(reverse('customers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/customers.html')

    def test_successful_transaction(self):
        response = self.client.post(reverse('customers'), {
            'sender_id': str(self.customer1.id),
            'receiver': str(self.customer2.id),
            'amount': '100.00'
        })
        self.assertRedirects(response, reverse('customers'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Transaction successful!')
        
        # Refresh customers from database
        self.customer1.refresh_from_db()
        self.customer2.refresh_from_db()
        
        self.assertEqual(self.customer1.balance, Decimal('900.00'))
        self.assertEqual(self.customer2.balance, Decimal('600.00'))

    def test_insufficient_balance(self):
        response = self.client.post(reverse('customers'), {
            'sender_id': str(self.customer1.id),
            'receiver': str(self.customer2.id),
            'amount': '2000.00'
        })
        self.assertRedirects(response, reverse('customers'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Insufficient balance.')

    def test_invalid_receiver(self):
        response = self.client.post(reverse('customers'), {
            'sender_id': str(self.customer1.id),
            'receiver': 'invalid-uuid',
            'amount': '100.00'
        })
        self.assertRedirects(response, reverse('customers'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Invalid receiver ID format.')

    def test_same_sender_receiver(self):
        response = self.client.post(reverse('customers'), {
            'sender_id': str(self.customer1.id),
            'receiver': str(self.customer1.id),
            'amount': '100.00'
        })
        self.assertRedirects(response, reverse('customers'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "The sender and receiver are the same; it can't be done.")

    def test_invalid_amount(self):
        response = self.client.post(reverse('customers'), {
            'sender_id': str(self.customer1.id),
            'receiver': str(self.customer2.id),
            'amount': 'invalid'
        })
        self.assertRedirects(response, reverse('customers'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Invalid amount. Please enter a valid number.')