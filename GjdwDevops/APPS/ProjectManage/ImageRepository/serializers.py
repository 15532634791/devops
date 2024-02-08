from rest_framework import serializers
from .models import ImageRepoModel, File


class ImageRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageRepoModel
        # fields = ['id', 'name', 'age']
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
