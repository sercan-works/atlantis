import subprocess
from celery.task import periodic_task
from celery.schedules import crontab

@periodic_task(run_every=(crontab(minute='*/1')))
def ping_ip():
    try:
        output = subprocess.check_output(['ping', '-c', '1', '192.168.1.1'])
        print(output)
    except subprocess.CalledProcessError as e:
        print("Ping Failed:", e.output)