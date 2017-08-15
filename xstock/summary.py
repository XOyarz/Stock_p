from django.shortcuts import render
from xstock.models import Portfolio, Wallet

def summary(request):

    all = Portfolio.objects.filter(user=request.user) # filter all transactions by user
    symbols = [] # generate list of all symbols
    for a in all:
        symbols.append(a.symbol)
    uniques = set(symbols) #create a set to get uniques

    summary_dict = {} # initiate empty dictionary
    for i in uniques:
        by_symbol = Portfolio.objects.filter(user=request.user, symbol=i) # Get all transactions by stock
        total = 0 # initiate total number of shares
        for each in by_symbol:
            total += each.shares
        summary_dict[each.symbol] = total

    cash = Wallet.objects.get(user=request.user)
    cash = cash.wallet
    print(cash)

    return render(request, 'xstock/summary.html', {'summary': summary_dict, 'cash':cash})
