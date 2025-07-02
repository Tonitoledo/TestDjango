from rest_framework import serializers
from crud.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Invoice
        fields = ['ref', 'numberInvoice', 'title', 'customer', 'date', 'total']
