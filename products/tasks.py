from celery import shared_task
from django.core.management import call_command
from .models import Product
import logging

logger = logging.getLogger(__name__)

@shared_task
def check_product_stock():
    products = Product.objects.filter(stock__lt=10)
    for product in products:
        logger.warning(f'Product {product.name} (SKU: {product.sku}) has low stock: {product.stock}')
