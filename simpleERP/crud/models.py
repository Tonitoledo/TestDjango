from django.db import models
from django.utils.translation import gettext_lazy as _

class Invoice(models.Model):
    ref = models.CharField(max_length=10, blank=True, verbose_name=_("Serie de factura"))
    numberInvoice = models.IntegerField(default=1, unique=True, verbose_name=_("Número de factura"))
    title = models.CharField(max_length=100, blank=True, verbose_name=_("Titulo"))
    description = models.TextField(blank=True, verbose_name=_("Descripcion"))
    customer = models.CharField(max_length=100, blank=True, verbose_name=_("cliente"))
    date = models.DateField(verbose_name=_("Fecha de creación"))
    total = models.DecimalField(max_digits=24, decimal_places=2, default=0.00, verbose_name=_("Total"))
    lastUpdated = models.DateTimeField(auto_now=True, verbose_name=_("Última modificación"))

    class Meta:
        verbose_name = _("Factura")
        verbose_name_plural = _("Facturas")
        ordering = ['-lastUpdated']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['customer']),
            models.Index(fields=['date']),
            models.Index(fields=['total']),
        ]
    
    def __str__(self):
        return self.title

class LineInvoice(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='lines')
    unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def subtotal(self):
        return self.unit * self.price

