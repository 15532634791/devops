from django.db import models
from APPS.Login.models import User


class RdsDatabaseResourceInfo(models.Model):
    """
    RDS数据库资源信息
    """
    organization = models.CharField(max_length=255, help_text="组织")
    systemName = models.CharField(max_length=255, help_text="系统名称")
    instanceId = models.CharField(max_length=255, help_text="实例id")
    instanceIp = models.CharField(max_length=255, help_text="实例ip")
    instanceName = models.CharField(max_length=255, help_text="实例名称")
    internalNetworkAddress = models.CharField(max_length=255, help_text="内网地址")
    port = models.IntegerField(help_text="端口号")
    cpu = models.CharField(max_length=255, help_text="CPU核数")
    diskSpace = models.CharField(max_length=255, help_text="磁盘空间")
    memory = models.CharField(max_length=255, help_text="内存")
    connectNumber = models.IntegerField(help_text="连接数")
    IOPS = models.CharField(max_length=255, help_text="IOPS")
    creationTime = models.DateTimeField(max_length=255, help_text="创建时间")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class RdsInstanceInfo(models.Model):
    """
    RDS实例账号 数据库信息
    """
    instanceId = models.CharField(max_length=255, help_text="实例id")
    account = models.CharField(max_length=255, help_text="账号")
    instanceType = models.CharField(max_length=255, help_text="实例类型")
    instanceStatus = models.CharField(max_length=255, help_text="实例状态")
    affiliation = models.CharField(max_length=255, help_text="所属")
    affiliationData = models.CharField(max_length=255, help_text="所属数据")
    accountDescription = models.CharField(max_length=255, help_text="账号描述")
    characterSet = models.CharField(max_length=255, help_text="字符集")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class RdsDatabaseMonitor(models.Model):
    """
    RDS数据库监控信息
    """
    instanceId = models.CharField(max_length=255, help_text="实例id")
    instanceName = models.CharField(max_length=255, help_text="实例名称")
    cpuUtilization = models.CharField(max_length=255, help_text="cpu利用率")
    memoryUtilization = models.CharField(max_length=255, help_text="内存利用率")
    diskUtilization = models.CharField(max_length=255, help_text="硬盘利用率")
    connectUtilization = models.CharField(max_length=255, help_text="连接利用率")
    iopsUsage = models.CharField(max_length=255, help_text="IOPS使用率")
    QPS = models.CharField(max_length=255, help_text="QPS")
    networkIncomingTraffic = models.CharField(max_length=255, help_text="网络入流量")
    networkOutTraffic = models.CharField(max_length=255, help_text="网络出流量")
    mainBackupDelay = models.CharField(max_length=255, help_text="主备延迟")
    activeStandbySwitching = models.CharField(max_length=255, help_text="主备切换")
    numberOfTableLocks = models.CharField(max_length=255, help_text="表锁个数")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)