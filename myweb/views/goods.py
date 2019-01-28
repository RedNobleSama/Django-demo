from django.shortcuts import reverse,redirect,render
from common.models import *

def web_goodlist(request):
    type = Type.objects.all()
    goods = Goods.objects.all()
    tid = int(request.GET.get('tid'))
    list = goods.filter(types_id__in=Type.objects.only('id').filter(id=tid))
    context ={
        'typelist':type,
        'goodlist':list
    }
    return render(request,'myweb/goods/goodlist.html',context)

def web_good_details(request,uid):
    type = Type.objects.all()
    goods = Goods.objects.get(id=uid)
    context ={
        'goodlist':goods,
        'typelist':type
    }
    return render(request,'myweb/goods/details.html',context)
