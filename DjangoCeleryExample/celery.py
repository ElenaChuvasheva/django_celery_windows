import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoCeleryExample.settings")
# app = Celery("DjangoCeleryExample", broker="amqp://localhost:5672")
app = Celery("DjangoCeleryExample")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs) -> None:
    sender.add_periodic_task(3, periodic_task.s(), name="Periodic task example")

@app.task(name="PeriodicTask (every 3 seconds)")
def periodic_task() -> None:
    print("Example of periodic task executed!")
