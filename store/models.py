from datetime import datetime
import email
from itertools import product
from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models


class Promotion(models.Model):
    description=models.CharField(max_length=255,null=True)
    discount=models.FloatField(null=True)

class Collection(models.Model):
    title=models.CharField(max_length=255,null=True)

class Product(models.Model):
    slug=models.SlugField(null=True)
    title=models.CharField(max_length=255,null=True)
    description=models.TextField(null=True)
    unit_price=models.DecimalField(max_digits=6,decimal_places=2,null=True)
    inventory=models.IntegerField(null=True)
    last_update=models.DateTimeField(auto_now=True,null=True)
    collection=models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotions=models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name=models.CharField(max_length=255,null=True)
    last_name=models.CharField(max_length=255,null=True)
    email=models.EmailField(unique=True,null=True)
    phone=models.CharField(max_length=255,null=True)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_PENDING='P'
    PAYMENT_COMPLETE='C'
    PAYMENT_FAILED='F'
    PAYMENT_STUTUS_CHOICE=[
        (PAYMENT_PENDING,'Pending'),
        (PAYMENT_COMPLETE,'Complete'),
        (PAYMENT_FAILED,'Failed')
    ]
    placed_at=models.DateTimeField(auto_now_add=True,null=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STUTUS_CHOICE,default=PAYMENT_PENDING)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.SmallIntegerField(null=True)
    unit_price=models.DecimalField(max_digits=6,decimal_places=2,null=True)


class Address(models.Model):
    street=models.CharField(max_length=255,null=True)
    city=models.CharField(max_length=255,null=True)
    zip=models.IntegerField(null=True)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)


class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField(null=True)
