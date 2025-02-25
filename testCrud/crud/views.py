from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm


def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.save()
            return redirect('crud:crud_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoice_create.html', {'form': form})

def invoice_list(request):
    try:
        if request.method == "GET":
            return get(request)
    except Exception as e:
        return HttpResponse(str(e))
        

def get(request):
    form = InvoiceForm()
    invoices_not_download = Invoice.objects.filter(isDownload=False)
    invoices_download = Invoice.objects.filter(isDownload=True)

    return render(request, 'invoice_list.html', {
        'form':form,
        'invoices_not_download': invoices_not_download,
        'invoices_download':invoices_download
    })