from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    isAdmin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    lastUpdated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.username

