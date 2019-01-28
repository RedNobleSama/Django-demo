from django.shortcuts import reverse,redirect,render
from common.models import *
from myweb.views.index import *



def web_cart(request,uid):
    if request.session.get('user',None):
        user = User.objects.get(id=request.session['id'])
        type= Type.objects.all()
        goods = Goods.objects.get(id=uid)
        context={
            'typelist':type,
            'goodlist':goods,
            'userlist':user
        }
        return render(request, 'myweb/cart/cart.html', context)
    else:
        return redirect(reverse(web_login))

def web_insertcart(request,uid):
    if request.session.get('user', None):
        goods = Goods.objects.get(id=uid)
        type = Type.objects.all()

        context = {
            'goodlist': goods,
            'typelist': type,
        }
        orders = Orders()
        orders.uid = request.session['id']
        orders.linkman =request.POST['linkman']
        orders.address = request.POST['address']
        orders.tel = request.POST['tel']
        orders.save()

        order = Orders.objects.all()
        context2 ={
            'orderlist':order
        }
        return render(request,'myweb/cart/cart2.html',context,context2)
    else:
        return redirect(reverse(web_login))

def web_insertcart2(request,uid):
    if request.session.get('user', None):
        od = Details()
        od.order_id =request.POST['order_id']
        od.goods_id =request.POST['goods_id']
        od.book = request.POST['book']
        od.price = request.POST['price']
        od.save()

        ods = Details.objects.get(id=uid)
        context ={
            'odlist':ods
        }
        return render(request, 'myweb/cart/success.html', context)
    else:
        return redirect(reverse(web_login))