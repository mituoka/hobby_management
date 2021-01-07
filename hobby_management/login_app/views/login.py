from django.shortcuts import render,redirect
from django.urls import reverse

def main_login(request):

    param = {
        'a':'1',
    }

    if (request.method == 'GET'):
        print(10)
    elif (request.method == 'POST'):
        print(20)
        redirect_url = reverse('menu')
        
        url = f'{redirect_url}'
        print(redirect_url)
        print(url)
        return redirect('menu')

    return render(request, 'login.html',param)

def login_bottom_push(request):
    
    param = {
        'a':'1',
    }

    if (request.method == 'GET'):
        print(30)
    elif (request.method == 'POST'):
        print(40)

    return render(request, 'menu.html',param)