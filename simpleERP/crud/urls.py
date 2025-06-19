from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('form-create/', views.create_invoice, name='invoice_create'),
    #path('create-save/', views.invoice_save, name='invoice_save'),
    #path('invoice-delete/', views.invoice_del, name='invoice_delete'),
    path('list/', views.invoice_list, name='invoice_list'),

    # API Invoices
    path("api/invoices/", views.invoice_list_api, name="invoice_list_api"),
]