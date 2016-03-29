from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import *

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
class BaseProductSerializer(serializers.HyperlinkedModelSerializer):
    seller = SellerSerializer()
    class Meta:
        model = Product
        fields = ('product_id', 'name', 'description','related_products',
                   'unit', 'price_per_unit','max_available_units','quality_remarks','origin','seller')
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    related_products = BaseProductSerializer(many=True)
    seller = SellerSerializer()
    class Meta:
        model = Product
        fields = ('product_id', 'name', 'description','related_products',
                   'unit', 'price_per_unit','max_available_units','quality_remarks','origin','seller')
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
class CartitemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cartitem
        fields=('cartitem_id','cart','qty','product','price_perunit')
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    seller = SellerSerializer()
    class Meta:
        model = Order
        fields = ('order_id','seller','subtotal','payment','delivery_time')
class OrderitemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orderitem
        fields = ('orderitem_id','order','unit','qty_in_units','price_perunit','product')