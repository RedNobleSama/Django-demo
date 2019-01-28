from django.shortcuts import redirect,render,reverse
from common.models import *
from django.http import HttpResponse
from PIL import Image
import time,os

def myadmin_goodlist(request):
    if request.session.get('user', None):
        goods = Goods.objects.all()
        context ={'goodlist':goods}
        return render(request,'myadmin/goods/goodlist.html',context)
    else:
        return render(request,'myadmin/login.htm')


def myadmin_addgood(request):
    if request.session.get('user', None):
        type =Type.objects.all()
        context ={'typelist':type}
        return render(request, 'myadmin/goods/addgoods.html',context)
    else:
        return render(request, 'myadmin/login.htm')


def myadmin_insertgood(request):
    myfile = request.FILES.get("picture", None)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/pics/original/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    # 执行图片缩放
    im = Image.open("./static/pics/original/" + filename)  # 打开图片

    # 缩放到360*480(缩放后的宽高比例不变):
    im.thumbnail((360, 360))
    im.save("./static/pics/details_L/" + filename, None)  # 商城详情页大图

    # 缩放到285*407(缩放后的宽高比例不变):
    im.thumbnail((215, 215))
    im.save("./static/pics/details_s/" + filename, None)  # 商城列表页图

    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((75, 75))
    im.save("./static/pics/cart/" + filename, None)  # 商城列表页图

    goods = Goods()
    goods.types_name = request.POST['types_name']
    goods.types_id = request.POST['types_id']
    goods.book = request.POST['book']
    goods.company = request.POST['company']
    goods.author = request.POST['author']
    goods.picture = filename
    goods.price = request.POST['price']
    goods.content =request.POST['content']
    goods.present = request.POST['present']
    goods.save()
    return redirect(reverse(myadmin_goodlist))

def myadmin_updategood(request,uid):
    if request.session.get('user', None):
        type =Type.objects.all()
        goods = Goods.objects.get(id=uid)
        context ={'typelist':type,'goodlist':goods}
        return render(request, 'myadmin/goods/updategoods.html',context)
    else:
        return render(request, 'myadmin/login.htm')


def myadmin_editgood(request,uid):
    goods = Goods.objects.get(id=uid)

    myfile = request.FILES.get("picture", None)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/pics/original/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    # 执行图片缩放
    im = Image.open("./static/pics/original/" + filename)  # 打开图片

    # 缩放到360*480(缩放后的宽高比例不变):
    im.thumbnail((350, 500))
    im.save("./static/pics/details_L/" + filename, None)  # 商城详情页大图

    # 缩放到86*115(缩放后的宽高比例不变):
    im.thumbnail((120, 120))
    im.save("./static/pics/details_s/" + filename, None)  # 商城详情页小图

    # 缩放到75*75(缩放后的宽高比例不变):
    im.thumbnail((52.5, 75))
    im.save("./static/pics/cart/" + filename, None)  # 商城列表页图

    # 删除原图片
    img1 = "./static/pics/original/" + goods.picture
    img2 = "./static/pics/details_s/" + goods.picture
    img5 = "./static/pics/cart/"+ goods.picture
    img6 = "./static/pics/details_L/"+ goods.picture

    if os.path.exists(img1):
        os.remove(img1)
    if os.path.exists(img2):
        os.remove(img2)
    if os.path.exists(img5):
        os.remove(img5)
    if os.path.exists(img6):
        os.remove(img6)

    goods.types_name = request.POST['types_name']
    goods.types_id = request.POST['types_id']
    goods.book = request.POST['book']
    goods.company = request.POST['company']
    goods.author = request.POST['author']
    goods.picture = filename
    goods.price = request.POST['price']
    goods.content = request.POST['content']
    goods.present = request.POST['present']
    goods.save()
    return redirect(reverse(myadmin_goodlist))



def myadmin_deletegood(request,uid):
    goods = Goods.objects.get(id=uid)

    img1 = "./static/pics/original/" + goods.picture
    img2 = "./static/pics/details_s/" + goods.picture
    img3 = "./static/pics/details_L/" + goods.picture
    img5 = "./static/pics/cart/" + goods.picture

    if os.path.exists(img1):
        os.remove(img1)
    if os.path.exists(img2):
        os.remove(img2)
    if os.path.exists(img3):
        os.remove(img3)
    if os.path.exists(img5):
        os.remove(img5)

    goods.delete()
    return redirect(reverse(myadmin_goodlist))
