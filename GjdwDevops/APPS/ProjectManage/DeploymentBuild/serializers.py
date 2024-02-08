from rest_framework import serializers
from .models import DeployBuildFile, DeployBuildModel


class DeployBuildModelSerializer(serializers.ModelSerializer):
    """
    序列化器
    """
    class Meta:
        model = DeployBuildModel
        fields = '__all__'


class DeployBuildFileSerializer(serializers.ModelSerializer):
    """
    上传文件
    """
    class Meta:
        model = DeployBuildFile
        fields = '__all__'

