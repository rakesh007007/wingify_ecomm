from django.contrib import admin
from app.models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	admin.site.register(User)
	admin.site.register(Address)
	admin.site.register(Category)
	admin.site.register(Product)
	admin.site.register(Cart)
	admin.site.register(Cartitem)
	admin.site.register(Order)
	admin.site.register(Orderitem)
	admin.site.register(Seller)