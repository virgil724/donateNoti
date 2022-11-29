from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.conf import settings
import logging
import os


# 日志配置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=os.path.join(settings.MEDIA_ROOT, 'log', 'scheduler.log'),
                    filemode='a')

# 实例化调度器
sched = BackgroundScheduler()
# 调度器使用默认的DjangoJobStore()
sched.add_jobstore(DjangoJobStore(), 'default')
sched._logger = logging
# 注册事件。启用时会报外键引用错误，原因待查。。。
# register_events(sched)
sched.start()
