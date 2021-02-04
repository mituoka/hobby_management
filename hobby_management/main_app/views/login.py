from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .form import login_form as form_class
import logging


def main_login(request):

    params = {
        'username':'ユーザー名',
        'password':'パスワード',
        'form':form_class.login_form,
        'login_bottom':'ログイン',
    }
    
    logger = logging.getLogger('debug')

    print(request.method)    

    if (request.method == 'GET'):
        logger.debug(request.method)
    elif (request.method == 'POST'):
        logger.debug(request.method)

        username=request.POST['username']
        password=request.POST['password']
    
        try:
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('menu')
            else:
                params['message']='ユーザーIDまたはパスワードが間違っています'                
        except :
            params[message]="ユーザー認証に失敗しました。"

            
    return render(request, 'login.html',params)

def login_bottom_push(request):
    
    params = {
        'a':'1',
    }


    if (request.method == 'POST'):
        print(30)



    return render(request, 'menu.html',params)
