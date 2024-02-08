from rest_framework import serializers
from .models import DepartmentResourceGroup, Namespace


class DepartmentResourceGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentResourceGroup
        fields = '__all__'


class NamespaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Namespace
        fields = '__all__'
