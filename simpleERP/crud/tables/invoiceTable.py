import django_tables2 as tables
from crud.models import Invoice
from django.utils.html import format_html
from django.urls import reverse

class InvoiceTable(tables.Table):
    #actions = tables.Column(
    #    empty_values=(), 
    #    orderable=False, 
    #    verbose_name='Acciones',
    #    attrs={
    #        'td': {'class': 'text-nowrap actions-td'}
    #    }
    #)

    class Meta:
        model = Invoice
        template_name = "django_tables2/bootstrap5.html"
        fields = (
            'ref',
            'numberInvoice',
            'title',
            'customer',
            'total',
            'date',
        )
        attrs = {
            'class': 'table table-hover table-striped',
            'thead': {'class': 'thead-dark'},
        }
       
        row_attrs = {
            'data-href': lambda record : reverse('crud:invoice_edit', kwargs={'pk': record.pk}),
            'id': 'clickable-row',
            'class': 'clickable-row'
        }
        
    #def render_actions(self, record):
    #    return format_html(
    #        '<a href="{}" class="btn btn-sm btn-warning">Editar</a>',
    #        reverse('crud:invoice_edit', kwargs={'id': record.pk})
    #    )