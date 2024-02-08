from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    序列化器
    """
    class Meta:
        model = User
        fields = '__all__'
