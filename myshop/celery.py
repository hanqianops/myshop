from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# 为 Celery 命令行程序设置了 DJANGO_SETTINGS_MODULE 变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

# 加载项目设置中任意的定制化配置
app.config_from_object('django.conf:settings')

# 在 NSTALLED_APPS 配置中的每个应用的路径下查找 tasks.py 来加载定义在其中的异步任务
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))