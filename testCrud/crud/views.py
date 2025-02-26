from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm



def invoice_list(request):
    try:
        if request.method == "GET":
            return get(request)
    except Exception as e:
        return HttpResponse(str(e))
    
def formInvoice_create(request):
    return render(request, "invoice_create.html") 

def invoice_save(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title:
            invoice = Invoice.objects.create(title=title, description=description)
            return JsonResponse({"success": True, "invoice_id": invoice.id})

    return render(request, 'invoice_create.html')        

def get(request):
    form = InvoiceForm()
    invoices_not_download = Invoice.objects.filter(isDownload=False)
    invoices_download = Invoice.objects.filter(isDownload=True)

    return render(request, 'invoice_list.html', {
        'form':form,
        'invoices_not_download': invoices_not_download,
        'invoices_download':invoices_download
    })