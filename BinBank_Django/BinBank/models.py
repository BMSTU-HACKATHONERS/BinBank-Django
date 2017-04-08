from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser


class Parent(models.Model):
    card_ID=models.CharField(verbose_name='card_id',max_length=255,default="")
    first_name=models.CharField(verbose_name='first_mane',max_length=255,default="")
    last_name=models.CharField(verbose_name='last_name',max_length=255,default="")
    phone=models.CharField(verbose_name='phone',max_length=255,default="")
    email=models.CharField(verbose_name='email',max_length=255,default="")
    balance=models.IntegerField(verbose_name='card_id',default=0)
    password = models.CharField(verbose_name='password', max_length=255, default="")


class Child(models.Model):
    #card_ID = models.CharField(verbose_name='card_id', max_length=255, default="")
    first_name = models.CharField(verbose_name='first_mane', max_length=255, default="")
    last_name = models.CharField(verbose_name='last_name', max_length=255, default="")
    phone = models.CharField(verbose_name='phone', max_length=255, default="")
    email = models.CharField(verbose_name='email', max_length=255, default="")
    balance = models.IntegerField(verbose_name='balance', default=0)
    parent_ID = models.ForeignKey(Parent,null=True)
    password=models.CharField(verbose_name='password', max_length=255, default="")
    #ограничения
    #биты
    online_cashing_bit=models.BooleanField(verbose_name='online_cashing_bit', default=False, db_index=True)
    #цифры
    max_per_day=models.IntegerField(verbose_name='max_per_day', default=0)
    max_payment=models.IntegerField(verbose_name='max_payment', default=0)
    low_balance=models.IntegerField(verbose_name='low_balance', default=0)
    max_cashing=models.IntegerField(verbose_name='max_cashing', default=0)

class Place(models.Model):
    child_ID=models.ForeignKey(Child,null=True)
    place_name=models.CharField(verbose_name='place_name', max_length=255, default="")
    longitude=models.FloatField(verbose_name='longtide',default=0)
    latitude = models.FloatField(verbose_name='latitide', default=0)
    enable_bit=models.BooleanField(verbose_name='enable_bit',default=True)

class Income(models.Model):
    child_ID=models.ForeignKey(Child,null=True)
    parent_ID=models.ForeignKey(Parent,null=True)
    sum=models.IntegerField(verbose_name='sum', default=0)
    type=models.IntegerField(verbose_name='type', default=0)

class Expense(models.Model):
    child_ID = models.ForeignKey(Child, null=True)
    sum=models.IntegerField(verbose_name='sum', default=0)
    type=models.IntegerField(verbose_name='type', default=0)

class IncomeType(models.Model):
    type=models.CharField(verbose_name='type', max_length=255, default="")

class ExpenseType(models.Model):
    type=models.CharField(verbose_name='type', max_length=255, default="")