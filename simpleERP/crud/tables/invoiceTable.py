import django_tables2 as tables
from crud.models import Invoice
from django.utils.html import format_html
from django.urls import reverse

class InvoiceTable(tables.Table):
    number = tables.Column(
        linkify=lambda record: reverse('invoice:detalle', args=[record.pk]),
        verbose_name='Número'
    )
    customer = tables.Column(accessor='cliente.nombre')

    class Meta:
        model = Invoice
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            'numero',
            'fecha_emision',
            'cliente',
            'total',
            'estado',
            'acciones'
        )
        attrs = {
            'class': 'table table-hover table-striped',
            'thead': {
                'class': 'thead-dark'
            }
        }