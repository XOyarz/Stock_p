from django.contrib import admin
from xstock.models import Portfolio, Wallet



class PortfolioModelAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'symbol', 'shares', 'user', 'action']

    list_display = ('name', 'price', 'symbol', 'shares', 'user', 'action')
    search_fields = ('name', 'symbol', 'action')

    class Meta:
        model = Portfolio

class WalletModelAdmin(admin.ModelAdmin):
    fields = ['user',  'wallet']
    list_display = ('user', 'wallet')
# Register your models here.
admin.site.register(Portfolio, PortfolioModelAdmin)
admin.site.register(Wallet, WalletModelAdmin)