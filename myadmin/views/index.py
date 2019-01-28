from django.shortcuts import redirect,render,reverse
from common.models import *

def myadmin_index(request):
    if request.session.get('user',None):
        return render(request,'myadmin/index.html')
    else:
        return render(request, 'myadmin/login.htm')


def myadmin_login(request):
    return render(request,'myadmin/login.htm')


def myadmin_dologin(request):
    user = User.objects.get(username=request.POST['username'])
    if user.password == request.POST['password']:
        request.session['user'] = user.username
        return redirect(reverse(myadmin_index))
    else:
        return render(request, 'myadmin/login.htm')



def myadmin_loginout(request):
    del request.session['user']
    return render(request, 'myadmin/login.htm')