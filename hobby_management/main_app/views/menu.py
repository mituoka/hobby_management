from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from ..models import Image
import json
from django.template.loader import render_to_string

# Create your views here.
@login_required
def menu_main(request):
    print('北')
    
    params = {
        'add_image_bottom':'新規追加',
    }

    #画像情報の取得
    object_list = Image.objects.all()
    
    #カテゴリーデータの取得
    categry_name=Image.objects.values_list('category_name', flat=True)
    
    # 重複するカテゴリーデータの取り除きソートする
    categry_list = set(categry_name)
    categry_list_sort=sorted(categry_list,reverse=True)

    # パラメーターに格納する
    params['categry_list']=categry_list
    params['object_list']=object_list

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

def search_category(request):
    # hoge = json.loads(request.POST.get("category_name"))
    select_category =request.POST.get("category_name")
    
    params = {
        'a':'1',
    }

    # object_list = Image.objects.values(category_name=select_category)
    object_list = Image.objects.filter(category_name=select_category)

    params['object_list']=object_list

    rendered_result = render_to_string('list.html', params)

    return JsonResponse({
        'html': rendered_result,
    })

def delete_image(request):
    # hoge = json.loads(request.POST.get("category_name"))
    image_id =request.POST.get("image_id")
    
    print(request.POST)
    
    params = {
        'a':'1',
    }

    # object_list = Image.objects.values(category_name=select_category)

    # 指定のデータを削除
    Image.objects.filter(id=image_id).delete()
    # object_list = Image.objects.all()

    # params['object_list']=object_list

    # rendered_result = render_to_string('list.html', params)

    return JsonResponse({
        'hoge': "hoge",
    })

