import os
from celery import Celery

# eventlet非常重要，Windows特有
# celery -A websocket_django  worker -l DEBUG -P eventlet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_django.settings')  # 设置django环境

app = Celery('websocket_django')  # 实例化一个app对象

app.config_from_object('django.conf:settings', namespace='CELERY')  # 使用CELERY_ 作为前缀，在settings中写配置

app.autodiscover_tasks()  # 发现任务文件每个app下的tasks.py文件
