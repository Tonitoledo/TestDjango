import logging
from django_tables2 import SingleTableMixin
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, View
from .models import Invoice
from .forms import InvoiceForm, LineInvoiceFormSet, ProductForm
from crud.tables.invoiceTable import InvoiceTable

logger = logging.getLogger(__name__)

class InvoiceListView(LoginRequiredMixin, SingleTableMixin, ListView):
    model = Invoice
    table_class = InvoiceTable
    template_name = 'invoice_list.html'
    paginate_by = 25
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-lastUpdated')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Facturas"
        return context
    
class InvoiceCreateView(LoginRequiredMixin, CreateView):
    form_class = InvoiceForm
    template_name = "invoice_create.html"
    success_url = reverse_lazy('crud:invoice_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = LineInvoiceFormSet(self.request.POST)
        else:
            context['formset'] = LineInvoiceFormSet()
        return context
    
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        
        if formset.is_valid():
            try:
                # Guardar la factura principal
                invoice = form.save(commit=False)
                invoice.title = self.assign_name_invoice(invoice)
                invoice.save()
                
                # Asociar y guardar las líneas
                formset.instance = invoice
                formset.save()
                
                # Actualizar total de la factura
                invoice.total = sum(line.subtotal for line in invoice.lines.all())
                invoice.save()
                
                return redirect(self.success_url)
                
            except Exception as e:
                logger.exception("Error al crear la factura")
                form.add_error(None, "Ocurrió un error interno al guardar la factura.")
                return self.render_to_response(self.get_context_data(form=form))
        else:
            logger.warning(f"Errores en el formset: {formset.errors}")
            return self.render_to_response(self.get_context_data(form=form))

    def assign_name_invoice(self, invoice):
        if invoice.ref and invoice.numberInvoice:
            return f"{invoice.ref}/{invoice.numberInvoice}"
        return invoice.title

class ProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = "product_create.html"
    success_url = reverse_lazy('crud:invoice_list')

    def form_valid(self, form):

        if form.is_valid():
            try:
                form.save()
                return redirect(self.success_url)
            
            except Exception as e:
                logger.exception("Error al crear el producto")
                form.add_error(None, "Ocurrió un error interno al guardar el producto.")
                return self.render_to_response(self.get_context_data(form=form))
            
        else:
            logger.warning(f"Errores en el formset: {form.errors}")
            return self.render_to_response(self.get_context_data(form=form))