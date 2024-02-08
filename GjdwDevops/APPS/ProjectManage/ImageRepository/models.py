import os
import time
from django.db import models


class ImageRepoModel(models.Model):
    repoId = models.IntegerField()
    repoName = models.CharField(max_length=255)
    repoNamespace = models.CharField(max_length=255)
    repoStatus = models.CharField(max_length=255)
    repoType = models.CharField(max_length=255)
    repoAuthorizeType = models.CharField(max_length=255)
    repoUrl = models.CharField(max_length=255)
    gmtModified = models.CharField(max_length=255)

    class Meta:
        db_table = 'image_repository'


def custom_upload_to(instance, filename):
    # 生成新的文件名，可以根据需要自定义

    # unique_ident = filename.split('____________________')
    # unique_dir_name = unique_ident[0]
    # origin_filename = unique_ident[1]
    # print(unique_dir_name, origin_filename)
    #
    # # 存放目录
    # storage_directory = os.path.join(
    #     os.getcwd(),
    #     'Media',
    #     'uploads',
    #     unique_dir_name
    # )
    #
    # if not os.path.exists(storage_directory):
    #     os.makedirs(storage_directory)
    #
    # if os.path.exists(
    #         os.path.join(storage_directory, origin_filename)
    # ):
    #
    #     os.remove(os.path.join(storage_directory, origin_filename))
    #     time.sleep(4)

    # 返回完整的文件路径
    return os.path.join('uploads/', filename)
    print( os.path.join(storage_directory, origin_filename))
    return os.path.join(storage_directory, origin_filename)


class File(models.Model):
    file = models.FileField(upload_to=custom_upload_to)
    # file = models.FileField(upload_to='uploads/')