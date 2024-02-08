from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import ArchitectureReviewModel, ArchitectureReviewModelDetail

class ArchitectureReviewModelSerializers(serializers.ModelSerializer):

    class Meta:
        model = ArchitectureReviewModel
        fields = '__all__'
        # exclude = ['pub_date']


class ArchitectureReviewModelDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = ArchitectureReviewModelDetail
        fields = '__all__'
        # exclude = ['pub_date']


class ArchitectureReviewModelView(ModelViewSet):
    queryset = ArchitectureReviewModel.objects.all()
    serializer_class = ArchitectureReviewModelSerializers


class ArchitectureReviewModelViewDetail(ModelViewSet):
    queryset = ArchitectureReviewModelDetail.objects.all()
    serializer_class = ArchitectureReviewModelDetailSerializers


