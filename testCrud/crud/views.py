from django.shortcuts import render
from .models import Invoice
from .forms import InvoiceForm

def invoice_list_and_create(request):
    form = InvoiceForm
    invoices = Invoice.objects.all()

    return render(request, 'invoice_list.html', {
        'form':form,
        'invoices':invoices
    })