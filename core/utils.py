import csv
import json
import pandas as pd
from decimal import Decimal
from django.db import transaction
from .models import Customer
import uuid

def import_customers(file_path):
    file_extension = file_path.split('.')[-1].lower()
    
    with transaction.atomic():
        if file_extension == 'csv':
            import_from_csv(file_path)
        elif file_extension == 'json':
            import_from_json(file_path)
        elif file_extension in ['xlsx', 'xls']:
            import_from_excel(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

def import_from_csv(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            create_or_update_customer(row)

def import_from_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for row in data:
            create_or_update_customer(row)

def import_from_excel(file_path):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        create_or_update_customer(row.to_dict())

def create_or_update_customer(data):
    customer, created = Customer.objects.update_or_create(
        id=uuid.UUID(data['ID']),
        defaults={
            'first_name': data['Name'].split()[0],
            'last_name': ' '.join(data['Name'].split()[1:]),
            'email': f"{data['Name'].replace(' ', '').lower()}@example.com",  # Generate a dummy email
            'balance': Decimal(data['Balance'])
        }
    )
    print(f"{'Created' if created else 'Updated'} customer: {customer}")
