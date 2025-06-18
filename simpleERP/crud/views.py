import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import Invoice
from .forms import InvoiceForm



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
    
def formInvoice_create(request):
    return render(request, "invoice_create.html") 

def post(request):
    if request.method == 'POST':
        if request.POST.get("action") == "create":
            invoice_save()
        elif request.POST.get("action") == "delete":
            invoice_del()
        #elif request.POST.get("action") == "update":
            #invoice_update()
    return render(request, 'invoice_create.html')

def invoice_save(request):
    title = request.POST.get("title")
    description = request.POST.get("description")
    if title:
        invoice = Invoice.objects.create(title=title, description=description)
        return JsonResponse({"success": True, "invoice_id": invoice.id})
            

def invoice_del(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            invoice_id = data.get("invoice_id")
            
            if Invoice.objects.filter(id=invoice_id).exists():
                Invoice.objects.filter(id=invoice_id).delete()
                return JsonResponse({"success": True})
            
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    
    return JsonResponse({"success": False})