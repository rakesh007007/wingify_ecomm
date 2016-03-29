from django.test import TestCase
from app.models import *
from django.utils import timezone
#test cases for modes start from here
class UserTest(TestCase):
	def create_user(self, mail_id="rak.dev007@gmail.com", mobile=8890108635, description="desc",password="hola123@"):
		return User.objects.create(mail_id=mail_id, mobile=mobile, description=description,password=password)
	def test_user_creation(self):
		w = self.create_user()
		self.assertTrue(isinstance(w, User))
		self.assertEqual(w.__unicode__(), str(w.user_id))
		self.assertEqual(w.mail_id, "rak.dev007@gmail.com")
		self.assertEqual(w.mobile,8890108635)
class OredrTest(TestCase):
	def create_order(self,payment_mode='online'):
		user = User.objects.create(mail_id="rak.dev007@gmail.com", mobile=8890108635, description="desc",password="hola123@")
		return Order.objects.create(payment_mode=payment_mode,user=user)
	def test_order_creation(self):
		w = self.create_order()
		self.assertTrue(isinstance(w, Order))
		self.assertEqual(w.__unicode__(), str(w.order_id))
		self.assertEqual(w.payment_mode, 'online')
class AddressTest(TestCase):
	def create_address(self, area="delhi", city="delhi", pincode=8812345555,state="NCR"):
		return Address.objects.create(area=area, city=city, pincode=pincode,state=state)
	def test_address_creation(self):
		w = self.create_address()
		self.assertTrue(isinstance(w, Address))
		self.assertEqual(w.__unicode__(), str(w.address_id))
class CategoryTest(TestCase):
	def create_category(self, name="Fruits", description="yo"):
		return Category.objects.create(name=name, description=description)
	def test_category_creation(self):
		w = self.create_category()
		self.assertTrue(isinstance(w, Category))
		self.assertEqual(w.__unicode__(), str(w.name))
class SellerTest(TestCase):
	def create_seller(self, name="Ram",mail_id="rak.dev007@gmail.com", mobile=8890108635,):
		return Seller.objects.create(name=name,mail_id=mail_id, mobile=mobile)
	def test_seller_creation(self):
		w = self.create_seller()
		self.assertTrue(isinstance(w, Seller))
		self.assertEqual(w.__unicode__(), str(w.name))
class ProductTest(TestCase):
	def create_product(self, name="Ram",price_per_unit=30):
		return Product.objects.create(name=name,price_per_unit=price_per_unit)
	def test_product_creation(self):
		w = self.create_product()
		self.assertTrue(isinstance(w, Product))
		self.assertEqual(w.__unicode__(), str(w.name))
		self.assertEqual(w.price_per_unit, 30)
class CartTest(TestCase):
	def create_cart(self):
		return Cart.objects.create()
	def test_product_creation(self):
		w = self.create_cart()
		self.assertTrue(isinstance(w, Cart))
		self.assertEqual(w.__unicode__(), str(w.cart_id))

