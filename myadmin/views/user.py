from django.shortcuts import redirect,render,reverse
from common.models import *


def myadmin_userlist(request):
    if request.session.get('user',None):
        user = User.objects.all()
        context ={'userlist':user}
        return render(request, 'myadmin/user/userlist.html',context)
    else:
        return render(request,'myadmin/login.htm')


def myadmin_adduser(request):
    if request.session.get('user', None):
        return render(request,'myadmin/user/adduser.html')
    else:
        return render(request,'myadmin/login.htm')


def myadmin_insertuser(request):
    user = User()
    user.username = request.POST['username']
    user.password = request.POST['password']
    user.name = request.POST['name']
    user.sex = request.POST['sex']
    user.address = request.POST['address']
    user.tel = request.POST['tel']
    user.email = request.POST['email']
    user.permissio = request.POST['permissio']
    user.save()
    return redirect(reverse(myadmin_userlist))

def myadmin_updateuser(request,uid):
    if request.session.get('user', None):
        user = User.objects.get(id=uid)
        context ={'userlist':user}
        return render(request, 'myadmin/user/updateuser.html',context)
    else:
        return render(request, 'myadmin/login.htm')


def myadmin_edituser(request,uid):
    user = User.objects.get(id=uid)
    user.username = request.POST['username']
    user.name = request.POST['name']
    user.sex = request.POST['sex']
    user.address = request.POST['address']
    user.tel = request.POST['tel']
    user.email = request.POST['email']
    user.permissio = request.POST['permissio']
    user.state = request.POST['state']
    user.save()
    return redirect(reverse(myadmin_userlist))


def myadmin_deleteuser(request,uid):
    user = User.objects.get(id=uid)
    user.delete()
    return redirect(reverse(myadmin_userlist))