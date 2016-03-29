from base import *
from rest_framework.parsers import *


class TokenView(APIView):
	def get(self, request, format=None):
		return Response({'detail': "GET Not Supported here"})
	def post(self, request, format=None):
		try:
			data = request.data
		except ParseError as error:
			return Response(
				'Invalid JSON - {0}'.format(error.detail),
				status=status.HTTP_400_BAD_REQUEST
			)
		if "user" not in data or "password" not in data:
			return Response({"result":"error","response":"Wrong credentials"}
				,
				status=status.HTTP_401_UNAUTHORIZED
			)
		user = request.data['user']
		user = str(user)
		password=request.data['password']
		password = str(password)
		if user=="publicapiconsumer1" and password=="givememyfuckingtoken":
			user = authUser.objects.first()
			token = Token.objects.get_or_create(user=user)
			return Response({"detail": "enjoy!!", "token": token[0].key})
		else:
			return Response({"detail": "fuck off!"})

 
		if not user:
			return Response(
				{"detail": "Kindly provide user details"},
				status=status.HTTP_404_NOT_FOUND
			)
class AddressViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
class CategoryViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = User.objects.all()
	serializer_class = UserSerializer
class CartViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Cart.objects.all()
	serializer_class = CartSerializer
class CartitemViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Cartitem.objects.all()
	serializer_class = CartitemSerializer
class OrderViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
class OrderitemViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Orderitem.objects.all()
	serializer_class = OrderitemSerializer
class ProductViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Product.objects.filter(status=1)
	serializer_class = ProductSerializer
class SellerViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows seller to be viewed or edited.
	"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	queryset = Seller.objects.all()
	serializer_class = SellerSerializer
class ProductSearchList(generics.ListAPIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	serializer_class = ProductSerializer

	def get_queryset(self):
		"""
		search api
		
		"""
		try:
			stext = self.kwargs['searchtext']
			return Product.rak.filter(description__icontains = stext)
		except:
			print 'error in ProductsBySearchcategory'