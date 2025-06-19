from django import forms 
from .models import Invoice, LineInvoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['ref','title', 'description', 'customer', 'date', 'total']
        widgets = {
            'ref': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'customer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Customer'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total'}),
        }

class LineInvoiceForm(forms.ModelForm):
    class Meta:
        model = LineInvoice
        fields = ['unit', 'price']
        widgets = {
            'unit': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }