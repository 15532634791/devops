from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import RdsDatabaseResourceInfoSerializer, RdsDatabaseMonitorSerializer, RdsInstanceInfoSerializer
from .models import RdsDatabaseResourceInfo, RdsDatabaseMonitor, RdsInstanceInfo
from rest_framework.permissions import IsAuthenticated
from Common.permissions import CommonPermissions


class RdsDatabaseResourceInfoView(ModelViewSet):
    queryset = RdsDatabaseResourceInfo.objects.all()
    serializer_class = RdsDatabaseResourceInfoSerializer

    permission_classes = [IsAuthenticated, CommonPermissions]


class RdsDatabaseMonitorView(ModelViewSet):
    queryset = RdsDatabaseMonitor.objects.all()
    serializer_class = RdsDatabaseMonitorSerializer

    permission_classes = []


class RdsInstanceInfoView(ModelViewSet):
    queryset = RdsInstanceInfo.objects.all()
    serializer_class = RdsInstanceInfoSerializer

    permission_classes = [IsAuthenticated, CommonPermissions]

    def get_queryset(self):
        # 获取当前登录用户
        user = self.request.user
        # 检查是否是管理员
        if user.is_superuser:
            # 如果是管理员，返回所有资源
            queryset = RdsInstanceInfo.objects.all()
        else:
            # 普通用户只返回他们自己创建的资源
            queryset = RdsInstanceInfo.objects.filter(created_by_id=user.id)
        return queryset



