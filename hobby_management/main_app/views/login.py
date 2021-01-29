from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def main_login(request):

    params = {
        'a':'1',
    }

    print(request.method)    

    if (request.method == 'GET'):
        print(10)
    elif (request.method == 'POST'):
        print(30)
        
        username=request.POST['username']
        password=request.POST['password']
        print("=============")
    
        try:
            # user = User.objects.create_user(username,'', password)
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                print('fsfsfsfs')
                return redirect('menu')
            else:
                params['message']='対象のユーザーが存在しません'
                
        except :
            print(30)
            print(params)
            params[message]="ユーザー認証に失敗しました。"

            
    return render(request, 'login.html',params)

def login_bottom_push(request):
    
    params = {
        'a':'1',
    }


    if (request.method == 'POST'):
        print(30)

        # ユーザー情報の確認


        # object_list = User.objects.all()
        # object_list = User.objects.get(username='test')
        # username=request.POST['username']
        # password=request.POST['password']
        # print(username)
        # print(password)
        # try:
        #     user = User.objects.create_user(username,'', password)
        # except :
        #     params[message] = '対象のユーザーが見つかりません'
        #     return redirect('login')

        # if user is not None:
        #     login(request, user)
        #     return redirect('menu')
        # else:
        #     return redirect('login')


    return render(request, 'menu.html',params)
