from __future__ import absolute_import
from celery import Celery
from TravelGuide import settings
import logging

app = Celery('TravelGuide', broker=settings.BROKER_URL)

# Get an instance of a logger
logger = logging.getLogger('django')

@app.task(bind=True)
def task_check_notifications(self):
    logger.info("============== BEGIN TASK CELERY: task_check_notifications")
    print "Check Notification"
    logger.info("============== END TASK CELERY: task_check_notifications")
    return
