from django.db import models

class Invoice(models.Model):
    ref = models.CharField(max_length=10, unique=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    customer = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-lastUpdated']
    
    def __str__(self):
        return self.title

class LineInvoice(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='lines')
    unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def subtotal(self):
        return self.unit * self.price

