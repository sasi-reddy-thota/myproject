from datetime import datetime
import email
from itertools import product
from pyexpat import model
from statistics import mode
from turtle import title
from unicodedata import name
from django.db import models


class Promotion(models.Model):
    description=models.CharField(max_length=255)
    discount=models.FloatField()

class Collection(models.Model):
    title=models.CharField(max_length=255)

class Product(models.Model):
    sku=models.CharField(max_length=10,primary_key=True)
    slug=models.SlugField(null=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)
    inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
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
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
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
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STUTUS_CHOICE,default=PAYMENT_PENDING)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity=models.SmallIntegerField()
    unit_price=models.DecimalField(max_digits=6,decimal_places=2)


class Address(models.Model):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    zip=models.IntegerField(null=True)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)


class Cart(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
