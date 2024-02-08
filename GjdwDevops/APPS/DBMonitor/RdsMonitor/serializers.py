from rest_framework import serializers
from .models import RdsDatabaseResourceInfo, RdsInstanceInfo, RdsDatabaseMonitor


class RdsDatabaseResourceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RdsDatabaseResourceInfo
        fields = '__all__'


class RdsInstanceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RdsInstanceInfo
        fields = '__all__'


class RdsDatabaseMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RdsDatabaseMonitor
        fields = '__all__'



