from django.urls import path
from . import views

app_name='crud'

urlpatterns = [
    path('form-create/', views.formInvoice_create, name='crud_create'),
    path('create-save/', views.invoice_save, name='invoice_save'),
    path('list/', views.invoice_list, name='crud_list')
]