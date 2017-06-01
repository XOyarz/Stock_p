from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'xstock/index.html')

def about(request):
    return HttpResponse("This is X-Stock Manager, a cool site that lets you manage your stock portfolio. "
                        "Hi /wdg/, don't forget to test it out or your mother will die in her sleep! <br/><a href='/xstock/'>Index</a>")

