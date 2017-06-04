from django import forms

class StockForm(forms.Form):
    search_term = forms.CharField(label='Search for Stock', max_length=30)
    share_amount = forms.IntegerField(label='How many shares')