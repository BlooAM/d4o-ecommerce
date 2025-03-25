import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd4o_ecommerce.settings')

app = Celery('d4o_ecommerce')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
