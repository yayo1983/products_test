from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'products_test.settings')

# Create a Celery application
app = Celery('products_test')

# Configure Celery using the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs
app.autodiscover_tasks()
