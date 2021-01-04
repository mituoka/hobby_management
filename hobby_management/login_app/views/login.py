from django.shortcuts import render


def main_login(request):

    param = {
        'a':'1',
    }

    if (request.method == 'GET'):
        print(10)
    elif (request.method == 'POST'):
        print(20)

    return render(request, 'login.html',param)