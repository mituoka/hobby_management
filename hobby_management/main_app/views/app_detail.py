from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Image

# Create your views here.
@login_required
def app_detail_main(request):
    
    params = {
        'a':'1',
    }        

    return render(request, 'app_detail.html',params)