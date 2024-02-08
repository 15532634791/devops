from django.db import models


class AppInstanceModel(models.Model):
    """
    应用列表模型
    """
    Dockerize = models.BooleanField(max_length=20, verbose_name='Dockerize')
    BuildPackageId = models.IntegerField(verbose_name='BuildPackageId')
    ClusterId = models.CharField(max_length=70, verbose_name='ClusterId')
    Memory = models.IntegerField(verbose_name='Memory')
    Port = models.IntegerField(verbose_name='Port')
    CreateTime = models.CharField(max_length=70, verbose_name='CreateTime')
    Cpu = models.IntegerField(verbose_name='Cpu')

    cluster_type_choice = ((5, "容器服务K8S集群"), (2, "ECS集群"))
    ClusterType = models.CharField(choices=cluster_type_choice, verbose_name="集群类型", max_length=30)

    Name = models.CharField(max_length=100, verbose_name="应用名")
    InstanceCount = models.IntegerField(verbose_name="实例总数")
    ApplicationType = models.CharField(max_length=200, verbose_name="ApplicationType", null=True)
    AppId = models.CharField(max_length=200, verbose_name="app id")
    RegionId = models.CharField(max_length=200, verbose_name="RegionId")
    RunningInstanceCount = models.IntegerField(verbose_name="RunningInstanceCount")

    class Meta:
        db_table = "app_instance"
