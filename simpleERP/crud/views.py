import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm, LineInvoiceForm


def invoice_list_api(request):
    invoices = Invoice.objects.all().values("id", "title", "description")
    return JsonResponse(list(invoices), safe=False)


def invoice_list(request):
    try:
        if request.method == "GET":
            return render(request, 'invoice_list.html')
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
    
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            print(form.data)
            invoice = Invoice(
                ref=form.cleaned_data['ref'],
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                customer=form.cleaned_data['customer'],
                date=form.cleaned_data['date'],
                total=form.cleaned_data['total']
            )
            print(invoice)
            invoice.save()
            return redirect('crud:invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'invoice_create.html', {'form': form})