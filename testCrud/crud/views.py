from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm

def invoice_list_and_create(request):
    try:
        if request.method == "POST":
            return post(request)
        else:
            return get(request)
    except Exception as e:
        return HttpResponse(str(e))
        
    

def post(request):
    form = InvoiceForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('crud:crud_list')

def get(request):
    form = InvoiceForm()
    invoices_not_download = Invoice.objects.filter(isDownload=False)
    invoices_download = Invoice.objects.filter(isDownload=True)

    return render(request, 'invoice_list.html', {
        'form':form,
        'invoices_not_download': invoices_not_download,
        'invoices_download':invoices_download
    })