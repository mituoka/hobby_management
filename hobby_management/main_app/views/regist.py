from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from ..models import Image
from .form import regist_form as form_class
# import imghdr

# Create your views here.
@login_required
def regist_main(request):
    
    params = {
        'title':'投稿画面',
        'category':'カテゴリー',
        'heading_name':'見出し名',
        'image_file':'画像ファイル',
        'comment':'コメント',
        'regist':'登録',
        'form':form_class.regist_form(),
    }

    print("regist_main成功")
    if (request.method == 'POST'):
        _category_name=request.POST["category_name"]
        _title_name=request.POST["heading_name"]
        _image_file=request.FILES["image_file"]
        _comment=request.POST["comment"]

        Image.objects.create(category_name=_category_name,title_name=_title_name,image_file=_image_file,comment=_comment)

        return redirect('menu')
    
    return render(request,'regist.html',params)