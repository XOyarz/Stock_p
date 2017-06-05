from django.contrib import admin
from xstock.models import Portfolio

class PortfolioModelAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'symbol', 'shares', 'user', 'action']

    list_display = ('name', 'price', 'symbol', 'shares', 'user', 'action')
    search_fields = ('name', 'symbol', 'action')

    class Meta:
        model = Portfolio


# Register your models here.
admin.site.register(Portfolio, PortfolioModelAdmin)