from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('customers/', views.customers, name='customers'),
    path('transactions/', views.transactions_history, name='transactions'),
        path('import-customers/', views.ImportCustomersView.as_view(), name='import_customers'),

]
