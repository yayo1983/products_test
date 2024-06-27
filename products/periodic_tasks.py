# api/periodic_tasks.py
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from datetime import timedelta
import json

# Define the schedule
schedule, created = IntervalSchedule.objects.get_or_create(
    every=1,
    period=IntervalSchedule.MINUTES,
)

# Create the periodic task
PeriodicTask.objects.get_or_create(
    interval=schedule,
    name='Check product stock every minute',
    task='api.tasks.check_product_stock',
    defaults={'kwargs': json.dumps({})}
)
