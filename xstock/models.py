from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(blank=True, max_digits=15, decimal_places=2)
    symbol = models.TextField(max_length=4)
    shares = models.IntegerField(blank=True)
    total_price = models.DecimalField(blank=True, max_digits=15, decimal_places=2)
    date = models.DateField(null=False)
    action = models.CharField(max_length=8)
    user = models.TextField(blank=True, max_length=30)

    def __str__(self):
        return self.name



class Wallet(models.Model):
    user = models.OneToOneField(User)
    wallet = models.DecimalField(max_digits=15, decimal_places=2, default=5000)

    def __str__(self):
        return self.user.wallet