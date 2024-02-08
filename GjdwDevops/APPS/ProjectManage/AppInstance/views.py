from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import AppInstanceModel
from .ListApplication import GetAppInstanceList
from .serializers import AppInstanceSerializer
from rest_framework import generics, status


class RefreshAppInstance(APIView):
    def get(self, request):
        app_instance_list = GetAppInstanceList()
        app_instance_list = app_instance_list.app_instance()

        for app_instance in app_instance_list:
            AppInstanceModel.objects.get_or_create(**app_instance)

        return Response()


class AppInstanceList(APIView):
    def get(self, request):
        app_ins_list = AppInstanceModel.objects.all()

        serializer = AppInstanceSerializer(data=app_ins_list, many=True)
        if serializer.is_valid():
            # print(serializer.data)
            pass

        return Response(serializer.data, status=status.HTTP_200_OK)
