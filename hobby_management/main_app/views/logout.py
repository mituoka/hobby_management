from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def logoutfunc(request):
    print('北')
    logout(request)
    return redirect('login')