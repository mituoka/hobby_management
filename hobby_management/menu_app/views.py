from django.shortcuts import render

# Create your views here.
def menu_main(request):
    
    params = {
        'a':'1',
    }

    print("成功")
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