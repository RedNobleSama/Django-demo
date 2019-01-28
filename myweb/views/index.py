from django.shortcuts import reverse,redirect,render
from common.models import *

def web_index(request):
    type = Type.objects.all()
    context ={'typelist':type}
    return render(request,'myweb/index.html',context)


def web_login(request):
    return render(request, 'myweb/user/login.html')


def web_dologin(request):
    user =User.objects.get(email=request.POST['email'])
    if user.password == request.POST['password']:
        request.session['user'] = user.username
        request.session['id'] = user.id
        return redirect(reverse(web_index))
    else:
        return render(request, 'myweb/index.html')


def web_loginout(request):
    del request.session['user']
    del request.session['id']
    return redirect(reverse(web_login))