from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

class Invoice(models.Model):
    ref = models.CharField(max_length=10, blank=True, verbose_name=_("Serie de factura"))
    numberInvoice = models.IntegerField(default=1, unique=True, verbose_name=_("Número de factura"))
    title = models.CharField(max_length=100, blank=True, verbose_name=_("Titulo"))
    customer = models.CharField(max_length=100, blank=True, verbose_name=_("cliente"))
    date = models.DateField(verbose_name=_("Fecha de creación"))
    total = models.DecimalField(max_digits=12, decimal_places=4, default=0.00, verbose_name=_("Total"))
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

    @property
    def subtotal(self):
        return sum(line.subtotal for line in self.lines.all())

class Product(models.Model):
    cod = models.CharField(max_length=6, unique=True, verbose_name=_("Codigo producto"))
    title = models.CharField(max_length=100, blank=True, verbose_name=_("Titulo"))
    description = models.TextField(blank=True, verbose_name=_("Descripcion"))
    price = models.DecimalField(max_digits=12, decimal_places=4, default=0.00, verbose_name=_("Precio"))

    def __str__(self):
        return f"{self.cod} - {self.title}"

class LineInvoice(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.DecimalField(max_digits=12, decimal_places=4, default = 0, validators=[MinValueValidator(0)])
    unit_price = models.DecimalField(max_digits=12, decimal_places=4, default= 0, validators=[MinValueValidator(0)])
    
    @property
    def subtotal(self):
        return self.quantity * self.unit_price