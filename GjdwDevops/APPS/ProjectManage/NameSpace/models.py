from django.db import models


class DepartmentResourceGroup(models.Model):
    Department = models.CharField(max_length=255, help_text='组织的id值')
    DepartmentName = models.CharField(max_length=255, help_text='组织名称')
    ResourceGroup = models.CharField(max_length=255, help_text='资源集的id值')
    ResourceGroupName = models.CharField(max_length=255, help_text='资源集名称')

    class Meta:
        db_table = 'DepartmentResourceGroup'


class Namespace(models.Model):
    authorizeType = models.CharField(max_length=255, help_text='认证类型')
    namespaceStatus = models.CharField(max_length=30, help_text='命名空间状态')
    namespaceName = models.CharField(max_length=255, help_text='命名空间名称')
    defaultVisibility = models.CharField(max_length=255, help_text='默认仓库类型')
    autoCreate = models.CharField(max_length=255, help_text='是否自动创建仓库')
    depart_resource = models.ForeignKey(DepartmentResourceGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Namespace'
