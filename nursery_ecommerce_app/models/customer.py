from django.db import models
from datetime import datetime
class Contact(models.Model):
    name = models.CharField(max_length=100)
    customer_need = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email