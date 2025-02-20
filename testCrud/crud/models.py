from django.db import models

class Invoice(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    isDownload = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title

