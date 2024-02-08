from rest_framework import serializers
from .models import AppInstanceModel


class AppInstanceSerializer(serializers.ModelSerializer):
    ClusterType_display = serializers.CharField(source='get_ClusterType_display', read_only=True)

    class Meta:
        model = AppInstanceModel
        fields = '__all__'
        # fields = ('ClusterType', 'ClusterType_display',)

    def get_ClusterType_display(self, obj):
        return obj.get_ClusterType_display()


