from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

# 加载项目设置中任意的定制化配置
app.config_from_object('django.conf:settings')

# 告诉 Celery 自动查找我们列举在 INSTALLED_APPS 设置中的异步应用任务
# Celery 将在每个应用路径下查找 tasks.py 来加载定义在其中的异步任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
