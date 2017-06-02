from django.shortcuts import render
from django.http import HttpResponse
from xstock.forms import StockForm
from xstock.helpers import *

# Create your views here.
def index(request):
    return render(request, 'xstock/index.html')

def about(request):
    return HttpResponse("This is X-Stock Manager, a cool site that lets you manage your stock portfolio. "
                        "Hi /wdg/, don't forget to test it out or your mother will die in her sleep! <br/><a href='/xstock/'>Index</a>")



def buy(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data##
            search_term = data['search_term']##mandatory data clean-up and retrieval from form

            quoted_stock = lookup(search_term)
            name = quoted_stock['name']
            price = quoted_stock['price']
            symbol = quoted_stock['symbol']
            #shares = quoted_stock['shares']
            shares = 2
            total_price = price * int(shares)

            context_dict = {'name':name, 'price':price, 'symbol':symbol, 'shares':shares, 'total_price':total_price}
            return render(request, 'xstock/buy2.html', context=context_dict)

    elif request.method == 'GET':
        form = StockForm()
        return render(request, 'xstock/buy.html', {'form':form})