from django.urls import path
from .views import InvoiceListView, InvoiceCreateView, ProductCreateView

app_name='crud'

urlpatterns = [
    # Invoices
    path('create-invoice/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('list/', InvoiceListView.as_view(), name='invoice_list'),

    # Products
    path('create-product/', ProductCreateView.as_view(), name='product_create'),
]