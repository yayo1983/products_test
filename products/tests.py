from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTests(APITestCase):
    def test_create_product(self):
        url = reverse('product-create')
        data = {'sku': '12345', 'name': 'Test Product'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().stock, 100)

    def test_update_stock(self):
        product = Product.objects.create(sku='12345', name='Test Product')
        url = reverse('update-stock', args=[product.id])
        data = {'stock': 50}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().stock, 150)

    def test_order_product(self):
        product = Product.objects.create(sku='12345', name='Test Product')
        url = reverse('order-create')
        data = {'product_id': product.id, 'quantity': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().stock, 90)

