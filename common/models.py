from django.db import models
from datetime import  datetime
# Create your models here.
#对应各表

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    permissio = models.IntegerField(default=1)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'user'

class Type(models.Model):
    goods_type = models.CharField(max_length=255)

    class Meta:
        db_table = 'type'

class Goods(models.Model):
    types_id = models.IntegerField()
    types_name = models.CharField(max_length=255)
    book = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    picture = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    present = models.TextField()
    content = models.TextField()

    class Meta:
        db_table = 'goods'

class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    addtime = models.DateTimeField(default=datetime.now())
    price = models.CharField(max_length=255)
    state = models.IntegerField(default=1)

    class Meta:
        db_table = 'orders'

class Details(models.Model):
    order_id = models.IntegerField()
    goods_id = models.IntegerField()
    book = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    class Meta:
        db_table = 'order_details'