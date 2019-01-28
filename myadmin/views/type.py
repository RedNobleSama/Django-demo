from django.shortcuts import reverse,redirect,render
from common.models import *

def myadmin_typelist(request):
    if request.session.get('user', None):
        type = Type.objects.all()
        context = {'typelist':type}
        return render(request,'myadmin/type/typelist.html',context)
    else:
        return render(request,'myadmin/login.htm')

def myadmin_addtype(request):
    if request.session.get('user', None):
        return render(request, 'myadmin/type/addtype.html')
    else:
        return render(request,'myadmin/login.htm')


def myadmin_inserttype(request):
    type = Type()
    type.goods_type =request.POST['goods_type']
    type.save()
    return redirect(reverse(myadmin_typelist))


def myadmin_updatetype(request,uid):
    if request.session.get('user', None):
        type = Type.objects.get(id=uid)
        context ={'typelist':type}
        return render(request,'myadmin/type/updatetype.html',context)
    else:
        return render(request,'myadmin/login.htm')


def myadmin_edittype(request,uid):
    type = Type.objects.get(id=uid)
    type.goods_type =request.POST['goods_type']
    type.save()
    return redirect(reverse(myadmin_typelist))


def myadmin_deletetype(reuqest,uid):
    type = Type.objects.get(id=uid)
    type.delete()
    return redirect(reverse(myadmin_typelist))

