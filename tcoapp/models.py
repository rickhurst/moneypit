from django.db import models


# Create your models here.
class Journey(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    miles = models.DecimalField(max_digits=10, decimal_places=2)
    litres = models.DecimalField(max_digits=10, decimal_places=2)
