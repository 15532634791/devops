import os
from django.db import models


class DeployBuildModel(models.Model):
    jarBuildName = models.CharField(max_length=255)
    jarBuildNameSpace = models.CharField(max_length=255)
    jarBuildRepo = models.CharField(max_length=255)
    jarBuildVersion = models.CharField(max_length=255)
    jarBuildCommand = models.TextField()
    jarBuildTime = models.CharField(max_length=255)
    jarBuildCommandStdout = models.TextField()
    jarBuildImageAddress = models.TextField()
    jarBuildStatus = models.CharField(max_length=255)
    jarBuildUser = models.CharField(max_length=255)

    class Meta:
        db_table = 'DeployBuild'


def custom_upload_to(instance, filename):
    # 生成新的文件名，可以根据需要自定义
    # print(filename)
    build_name = filename.split('_____')[0]
    namespace = filename.split('_____')[1]
    repo_name = filename.split('_____')[2]
    version = filename.split('_____')[3]
    origin_name = filename.split('_____')[4]
    # 存储目录
    storage_directory = '{}_{}_{}_{}'.format(
        build_name, namespace, repo_name, version
    )
    # 存放目录
    upload_directory = os.path.join(
        'DeployBuild/',
        storage_directory
    )

    # 返回完整的文件路径
    return os.path.join(upload_directory, origin_name)


class DeployBuildFile(models.Model):
    file = models.FileField(upload_to=custom_upload_to)