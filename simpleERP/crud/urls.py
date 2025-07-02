from django.urls import path
from .views import InvoiceListView, InvoiceCreateView, InvoiceEditView, ProductCreateView

app_name='crud'

urlpatterns = [
    # Invoices
    path('create-invoice/', InvoiceCreateView.as_view(), name='invoice_create'),
    path('invoice/<int:pk>/update/', InvoiceEditView.as_view(), name="invoice_edit"),
    path('list/', InvoiceListView.as_view(), name='invoice_list'),

    # Products
    path('create-product/', ProductCreateView.as_view(), name='product_create'),
]