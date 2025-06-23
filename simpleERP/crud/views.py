import logging
from django_tables2 import SingleTableMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView
from .models import Invoice
from .forms import InvoiceForm, LineInvoiceForm
from crud.tables.invoiceTable import InvoiceTable

logger = logging.getLogger(__name__)

class InvoiceListView(LoginRequiredMixin, SingleTableMixin, ListView):
    model = Invoice
    table_class = InvoiceTable
    template_name = 'crud/invoice_list.html'
    paginate_by = 25
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related('customer').order_by('-lastUpdated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Facturas"
        return context
    
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            try:
                invoice = form.save(commit=False)
                invoice.title = assign_name_invoice(invoice)
                invoice.save()
                return redirect('crud:invoice_list')
            except Exception as e:
                logger.exception("Error al crear la factura")  # Guarda en log
                form.add_error(None, "Ocurrió un error interno al guardar la factura.")  # Error no relacionado a un campo
        else:
            logger.warning(f"Formulario no válido: {form.errors}")
    else:
        form = InvoiceForm()
    return render(request, 'invoice_create.html', {'form': form})

def assign_name_invoice(invoice):
    serie = invoice.ref
    numInvoice = invoice.numberInvoice

    if serie != "" and numInvoice != 0:
        return serie + "/" + str(numInvoice)