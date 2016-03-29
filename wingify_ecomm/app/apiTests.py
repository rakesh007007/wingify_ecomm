#test cases for apis start from here
from django.test import TestCase
from app.models import *
from django.utils import timezone

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app.serializers import *
from django.contrib.auth.models import User as authUser
from rest_framework.authtoken.models import Token

class UserApiTest(APITestCase):
    def setUp(self):
        authUser.objects.create_superuser(username='admin', password='123', email='')
        user = authUser.objects.first()
        Token.objects.get_or_create(user=user)
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    def test_user_api(self):
        response = self.client.get('/api/user')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        response2 = self.client.get('/api/user/')
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        data = {"mail_id":"ssd","mobile":8890108635,"description":"description","password":"yola"}
        response3 = self.client.post('/api/user/',data,format='json')
        self.assertEqual(response3.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().mail_id, 'ssd')
class ProductApiTest(APITestCase):
    def setUp(self):
        authUser.objects.create_superuser(username='admin3', password='123', email='hhhg')
        user = authUser.objects.first()
        Token.objects.get_or_create(user=user)
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    def test_product_api(self):
        response = self.client.get('/api/product/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
