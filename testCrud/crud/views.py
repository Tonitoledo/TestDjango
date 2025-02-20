from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm

def invoice_list_and_create(request):

    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
    else:
        form = InvoiceForm()

    invoices = Invoice.objects.all()

    return render(request, 'invoice_list.html', {
        'form':form,
        'invoices':invoices
    })