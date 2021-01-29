from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..models import Image

# Create your views here.
@login_required
def menu_main(request):
    print('北')
    
    params = {
        'a':'1',
    }

    object_list = Image.objects.all()
    print(object_list)
    context_object_name = 'image_list'

    params['object_list']=object_list

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


    return render(request,'menu.html',params)

