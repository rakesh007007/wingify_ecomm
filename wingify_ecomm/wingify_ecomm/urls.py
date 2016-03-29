from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from wingify_ecomm import *
from wingify_ecomm.settings import *
from app.views import *
from app import apis
router = routers.DefaultRouter()
router.register(r'address', apis.AddressViewSet)
router.register(r'category', apis.CategoryViewSet)
router.register(r'product', apis.ProductViewSet)
router.register(r'user', apis.UserViewSet)
router.register(r'cart', apis.CartViewSet)
router.register(r'cartitem', apis.CartitemViewSet)
router.register(r'order', apis.OrderViewSet)
router.register(r'orderitem', apis.OrderitemViewSet)
router.register(r'seller', apis.SellerViewSet)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^api/search/product/(?P<searchtext>.+)/$', apis.ProductSearchList.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^authtoken/', apis.TokenView.as_view(), name='auth-view'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    ]