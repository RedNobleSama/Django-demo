from django.shortcuts import reverse,redirect,render
from common.models import *
from .index import *

def web_personal(request):
    user =User.objects.get(id = request.session['id'])
    context ={'userlist':user}
    return render(request,'myweb/user/personal.html',context)

def web_register(request):
    return render(request,'myweb/user/register.html')


def web_insertuser(request):
    password = request.POST['password']
    password1 = request.POST['password']
    if password == password1:
        user =User()
        user.username =request.POST['username']
        user.name =request.POST['name']
        user.email =request.POST['email']
        user.address =request.POST['address']
        user.tel =request.POST['tel']
        user.sex =request.POST['sex']
        user.password = request.POST['password']
        user.save()
        return redirect(reverse(web_login))
    else:
        return redirect(reverse(web_register))

def web_updatepassword(request):
    if request.session.get('user',None):
        user = User.objects.get(id=request.session['id'])
        context ={'userlist':user}
        return render(request,'myweb/user/updatepassword.html',context)
    else:
        return render(request, 'myweb/user/updatepassword.html')

def web_editpassword(request):
    if request.session.get('user',None):
        user = User.objects.get(id=request.session['id'])
        if user.email == request.POST['email']:
            return render(request,'myweb/user/updatepassword-2.html')
        else:
            return redirect(reverse(web_updatepassword))
    else:
        user  = User.objects.get(email=request.POST['email'])
        return redirect(reverse(web_editpassword2()))

def web_editpassword2(request):
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    if password1 == password2:
        if request.session.get('user',None):
            user = User.objects.get(id=request.session['id'])
            user.password = request.POST['password1']
            user.save()
            del request.session['user']
            del request.session['id']
            return redirect(reverse(web_login))
        else:
            return redirect(reverse(web_editpassword2))
    else:
        return redirect(reverse(web_editpassword2))

def web_update(request):
    pass

def web_edit(request):
    pass

