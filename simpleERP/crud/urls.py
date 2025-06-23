from django.urls import path
from .views import create_invoice, InvoiceListView

app_name='crud'

urlpatterns = [
    path('form-create/', create_invoice, name='invoice_create'),
    #path('create-save/', views.invoice_save, name='invoice_save'),
    #path('invoice-delete/', views.invoice_del, name='invoice_delete'),
    path('list/', InvoiceListView.as_view(), name='invoice_list'),
]