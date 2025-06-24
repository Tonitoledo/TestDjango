import django_tables2 as tables
from crud.models import Invoice
from django.utils.html import format_html
from django.urls import reverse

class InvoiceTable(tables.Table):
    class Meta:
        model = Invoice
        template_name = "django_tables2/bootstrap4.html"
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
            'thead': {
                'class': 'thead-dark'
            }
        }