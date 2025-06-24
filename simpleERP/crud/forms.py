from django import forms 
from .models import Invoice, LineInvoice, Product
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['ref', 'numberInvoice', 'title', 'customer', 'date']
        widgets = {
            'ref': forms.TextInput(attrs={
                'class': 'form-control', 
            }),
            'numberInvoice': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'customer': forms.TextInput(attrs={
                'class': 'form-control',  
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date'
            }),
        }
        labels = {
            'ref': _('Serie Factura'),
            'numberInvoice': _('Número Factura'),
            'title': _('Título'),
            'customer': _('Cliente'),
            'date': _('Fecha'),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['cod', 'title', 'description', 'price']
        widgets = {
            'cod': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'step': '0.0001',
            }),
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ordenar productos por código y mejorar la visualización
        self.fields['product'].queryset = Product.objects.all().order_by('cod')
        self.fields['product'].label_from_instance = lambda obj: f"{obj.cod} - {obj.title}"

class LineInvoiceForm(forms.ModelForm):
    class Meta:
        model = LineInvoice
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control select-product',
                'onchange': 'updateUnitPrice(this)'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control quantity-input',
                'min': '0',
                'step': '0.0001',
                'onchange': 'calculateLineTotal(this)'
            }),
            'unit_price': forms.NumberInput(attrs={
                'class': 'form-control unit-price-input',
                'min': '0',
                'step': '0.0001',
                'onchange': 'calculateLineTotal(this)'
            }),
        }

# Formset para las líneas de factura
LineInvoiceFormSet = inlineformset_factory(
    Invoice,
    LineInvoice,
    form=LineInvoiceForm,
    extra=1,
    can_delete=True
)