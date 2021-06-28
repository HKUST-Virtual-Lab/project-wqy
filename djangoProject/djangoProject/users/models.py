import time

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    org = models.CharField('Organization', max_length = 128, blank = True)

    telephone = models.CharField('Telephone', max_length = 50, blank = True)

    mod_date = models.DateTimeField('Last modified', auto_now=True)

    class Meta:
        verbose_name = 'User Profile'

    def __str__(self):
        return self.user.__str__()
# Create your models here.
# 郭廷章parts


def upload_path(instance, filename):  # 动态设置文件上传路径
    return 'uploads/{user_id}/{date}/{filename}'.format(
        user_id=instance.user_id,
        date=time.strftime('%Y/%m/%d', time.localtime()),
        filename=filename,
    )


def download_path(instance, filename):  # 动态设置实验结果路径
    return 'downloads/{date}/{filename}'.format(
        date=instance.date,
        filename=filename,
    )


class ExperimentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    duration = models.CharField(max_length=20)
    purpose = models.CharField(max_length=20)
    agentNumber = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=upload_path)  # 上传文件
    result = models.FilePathField(path=download_path)  # 实验结果
    user_id = models.CharField(max_length=20, default='114514')  # 上传者user的id——————作为外键使用
