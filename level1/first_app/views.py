from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Hello World, this is first app with include.")
    value = {'insert_me':"Hello, I am from views.py"}
    return render(request, 'first_app/index.html', context=value)

def help(request):
    value = {'help_msg':"Hello, I am help from views.py"}
    return render(request, 'first_app/help.html', context=value)