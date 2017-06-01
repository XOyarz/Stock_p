from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(blank=True, max_digits=15, decimal_places=2)
    symbol = models.TextField(max_length=4)
    shares = models.IntegerField(blank=True)
    total_price = models.DecimalField(blank=True, max_digits=15, decimal_places=2)
    date = models.DateField(null=False)
    user = models.IntegerField(blank=True)

    def __str__(self):
        return self.name