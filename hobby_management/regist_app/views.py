from django.shortcuts import render

# Create your views here.
def regist_main(request):
    
    params = {
        'a':'1',
    }

    print("regist_main成功")
    if (request.method == 'POST'):
        print(30)
        category_name=request.POST["category_name"]
        title_name=request.POST["title_name"]
        image_file=request.POST["image_file"]
        comment=request.POST["comment"]
        
        print(category_name)
        print(title_name)
        print(image_file)
        print(comment)

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


    return render(request, 'regist.html',params)