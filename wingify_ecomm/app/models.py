from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from wingify_ecomm import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your models here.

class Address(models.Model):
	address_id = models.AutoField(primary_key=True)
	area=models.CharField(max_length=300, null=True,blank=True,default='')
	city =models.CharField(max_length=300, null=True,blank=True, default='')
	state = models.CharField(max_length=300, null=True,blank=True,default='')
	pincode=models.IntegerField(null=True,blank=True)
	def __unicode__(self):
		return str(self.address_id)
	def addressId(self):
		return self.address_id
class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=300,blank=False,null=False)
	coverphoto = models.ImageField(blank=True,null=True)
	description =models.CharField(max_length=300,blank=False,null=False)
	def coverphotourl(self):
		return self.coverphoto.url
	def categoryId(self):
		return self.category_id
	def __unicode__(self):
		return str(self.name)
class Seller(models.Model):
    seller_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300, blank=False, null=False)
    mailid =models.CharField(max_length=300, blank=False, null=False,default='no mail id')
    mobile = models.BigIntegerField(blank=False,null=False)
    profile_pic = models.ImageField(blank=True,null=True,default='./No_image_available.png')
    address = models.ForeignKey(Address, blank=True, null=True)
    rating = models.FloatField(default=0)
    password = models.CharField(max_length=300, blank=False, null=False,default='pbkdf2_sha256$20000$xcPbF0CMVCyw$eZECZo2qDkuIVr8+UxTiIosfDPdHx6mMQNhUbp3AAjM=')
    status = models.FloatField(default=1)
    objects = models.Manager()
    def __unicode__(self):
    	return str(self.name)
    def sellerId(self):
    	return self.seller_id
class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	name=models.CharField(max_length=300,blank=False,null=False)
	description=models.TextField(blank=True,null=True,default='not available')
	category = models.ForeignKey(Category,blank=True,null=True,default=1)
	popularityIndex = models.FloatField(blank=True,null=True,default=1)
	unit = models.CharField(max_length=100,default='Kg')
	price_per_unit = models.FloatField(blank=False,null=False,default=0)
	coverphoto = models.ImageField(blank=True,null=True,default='./No_image_available.png')
	origin = models.CharField(max_length=300,null=True,blank=True,default='')
	max_available_units=models.FloatField(null=True,blank=True,default=100000)
	quality_remarks = models.TextField(null=True,blank=True,default='Custom Product')
	status = models.FloatField(blank=True,null=True,default=1)
	seller = models.ForeignKey(Seller,blank=True,null=True,default=1)
	related_products = models.ManyToManyField("self", blank=True)
	objects = models.Manager()
	def __unicode__(self):
		return str(self.name)+'-'+str(self.grade)+'-'+str(self.origin)
class Cart(models.Model):
	cart_id = models.AutoField(primary_key=True)
	#check this time thing
	time_of_create = models.DateTimeField(default=timezone.now,null=True,blank=True)
	time_of_update =models.DateTimeField(default=timezone.now,null=True,blank=True)
	cart_total = models.FloatField(default=0)
	class Meta:
		ordering = ['time_of_update']
	def __unicode__(self):
		return str(self.cart_id)
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    mail_id =models.CharField(max_length=300, blank=False, null=False)
    mobile = models.BigIntegerField(blank=False,null=False,unique=False)
    description = models.TextField(default='Not available')
    password = models.CharField(max_length=300, blank=False, null=False)
    profile_photo = models.ImageField(blank=False,null=False,default='./profile.gif')
    address = models.ForeignKey(Address, blank=True, null=True)
    cart =models.ForeignKey(Cart,blank=True,null=True)
    def cartId(self):
    	return self.cart.cart_id
    def userId(self):
		return self.user_id
    def addressId(self):
		return self.address.address_id

    def __unicode__(self):
    	return str(self.user_id)
    def save(self, *args, **kwargs):
    	if not self.pk:
    		ct = Cart()
    		ct.save()
    		self.cart=ct
    		self.password = make_password(self.password)
	    	super(User,self).save(*args, **kwargs)
        else:
	    	super(User,self).save(*args,**kwargs)
class Cartitem(models.Model):
	cartitem_id = models.AutoField(primary_key=True)
	cart=models.ForeignKey(Cart,blank=False,null=False)
	qty = models.FloatField()
	product = models.ForeignKey(Product,blank=False,null=False)
	price_perunit = models.FloatField(blank=False,null=False, default=0)
	time_of_create = models.DateTimeField(default=timezone.now,null=True,blank=True)
	time_of_update =models.DateTimeField(default=timezone.now,null=True,blank=True)
	class Meta:	
		ordering = ['-time_of_create']
	def cartItemId(self):
		return self.cartitem_id
	def __unicode__(self):
		return str(self.cartitem_id)
class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	user=models.ForeignKey(User,blank=False,null=False)
	time_of_create = models.DateTimeField(default=timezone.now,null=True,blank=True)
	time_of_update =models.DateTimeField(default=timezone.now,null=True,blank=True)
	payment_mode = models.CharField(max_length=200,blank=True,null=True)
	subtotal=models.FloatField(blank=True,null=True)
	payment=models.CharField(max_length=100,blank=True,null=True,default='unpaid')
	status = models.CharField(max_length=200,default='placed')
	order_msg = models.TextField(blank=True,null=True)
	delivery_time = models.DateField(blank=True,null=True)
	class Meta:	
		ordering = ['-delivery_time','-time_of_create']
	def orderId(self):
		return self.order_id
	def __unicode__(self):
		return str(self.order_id)+str(self.user.nameOfInstitution)
class Orderitem(models.Model):
	orderitem_id = models.AutoField(primary_key=True)
	order=models.ForeignKey(Order,blank=False,null=False)
	unit = models.CharField(max_length=100,default='kg')
	qty_in_units = models.FloatField()
	price_perunit = models.FloatField(blank=False,null=False)
	product = models.ForeignKey(Product,blank=False,null=False)
	def orderItemId(self):
		return self.orderitem_id
	def __unicode__(self):
		return str(self.orderitem_id)