from django.db import models

# Create your models here.
class Company(models.Model):
    C_name = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    type= models.CharField(max_length=100, choices=(('IT', 'IT'), ('NON-IT', 'NON-IT'), ('TRANSPORT', 'TRANSPORT')))
    add_date = models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)
