from django.shortcuts import render
from django.http import HttpResponse
from xstock.forms import StockForm
from xstock.helpers import *
from xstock.models import Portfolio, Wallet
import datetime
from decimal import Decimal
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    print(request.user)
    return render(request, 'xstock/index.html')


def about(request):
    x = Portfolio.objects.get(id=1)
    print(x.symbol)
    return HttpResponse("This is X-Stock Manager, a cool site that lets you manage your stock portfolio. "
                        "Hi /wdg/, don't forget to test it out or your mother will die in her sleep! <br/><a href='/xstock/'>Index</a>")


def history(request):
    hist = Portfolio.objects.filter(user=request.user)

    return render(request, 'xstock/history.html', {'obj':hist})


def summary(request):
    allx = Portfolio.objects.filter(user=request.user)
    uniques = []
    for a in allx:
        uniques.append(a.symbol)
    x = set(uniques)
    print(x)

    for i in x:
        by_symbol = Portfolio.objects.filter(user=request.user, symbol=i)
        print(by_symbol)
        total_shares = 0
        for tt in by_symbol:
            total_shares += tt.shares
        print(i, total_shares)
        symb_shares = {'symbol': i, 'shares':total_shares}


        #summed = sum(by_symbol.shares)
        #print(i, summed)
    return render(request, 'xstock/summary.html', )


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
            shares = data['share_amount']
            total_price = price * shares

            upWallet = Wallet.objects.get(user=request.user)
            upWallet.wallet -= Decimal(total_price)
            upWallet.save()

            user = str(request.user)
            context_dict = {'name':name, 'price':price, 'symbol':symbol, 'shares':shares, 'total_price':total_price, 'user':user}
            purchase(context_dict, user)
            return render(request, 'xstock/buy2.html', context=context_dict)

    elif request.method == 'GET':
        form = StockForm()
        return render(request, 'xstock/buy.html', {'form':form})


def purchase(stock_info, user):
    p = Portfolio(
        name=stock_info["name"],
        price=stock_info["price"],
        symbol=stock_info["symbol"],
        shares=stock_info["shares"],
        total_price=stock_info["total_price"],
        date=datetime.datetime.now(),
        action="BOUGHT",
        user=user
    )
    p.save()

