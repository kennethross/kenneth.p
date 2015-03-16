from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
#security concerns; cross relation request forgery
from django.core.context_processors import csrf

# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    #second parameter in the 'get' is for if the return variable 
    username = request.POST.get('username', '')
    password = request.POST.get('password', '') 
    user = auth.authenticate(username=username, password = password) 
    """
    #verification user
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('')
    """