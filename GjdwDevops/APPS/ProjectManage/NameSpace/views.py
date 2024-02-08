from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import DepartmentResourceGroup, Namespace
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import DepartmentResourceGroupSerializer, NamespaceSerializer
import os
from datetime import datetime
from .GetNamespaceList import NamespaceList, CreateNamespace


class NamespaceDepartmentResourceSync(APIView):
    def get(self, request):
        name_space = NamespaceList()
        data = name_space.get_department_resource()
        for ele in data:
            DepartmentResourceGroup.objects.get_or_create(**ele)

        # name_space = NamespaceList()
        data = name_space.get_department_resource_detail()
        for ele in data:
            # print(ele)
            depart_resource = DepartmentResourceGroup.objects.get(
                Department=ele.get('Department'),
                DepartmentName=ele.get('DepartmentName'),
                ResourceGroup=ele.get('ResourceGroup'),
                ResourceGroupName=ele.get('ResourceGroupName')
            )
            authorizeType = ele.get('authorizeType')
            namespaceStatus = ele.get('namespaceStatus')
            namespaceName = ele.get('namespace')
            defaultVisibility = ele.get('defaultVisibility')
            autoCreate = ele.get('autoCreate')

            Namespace.objects.get_or_create(
                authorizeType=authorizeType,
                namespaceStatus=namespaceStatus,
                namespaceName=namespaceName,
                defaultVisibility=defaultVisibility,
                autoCreate=autoCreate,
                depart_resource=depart_resource
            )
        return Response(
            {'status': 'success'}
        )


class DepartmentResource(APIView):
    def get(self, request):
        # name_space = NamespaceList()
        #
        # data = name_space.get_department_resource()
        # for ele in data:
        #     DepartmentResourceGroup.objects.get_or_create(**ele)

        depart_resource_list = DepartmentResourceGroup.objects.all()

        serializer = DepartmentResourceGroupSerializer(data=depart_resource_list, many=True)
        if serializer.is_valid():
            # print(serializer.data)
            pass

        return Response(serializer.data, status=200)

    def post(self, request):
        print(request.data)

        namespace = CreateNamespace()
        namespace.run(**request.data)

        return Response({'status': 'success'})


class DepartmentResourceDetail(APIView):
    def get(self, request):
        """
        创建数据
        :param request:
        :return:
        """
        # name_space = NamespaceList()
        # data = name_space.get_department_resource_detail()
        # for ele in data:
        #     # print(ele)
        #     depart_resource = DepartmentResourceGroup.objects.get(
        #         Department=ele.get('Department'),
        #         DepartmentName=ele.get('DepartmentName'),
        #         ResourceGroup=ele.get('ResourceGroup'),
        #         ResourceGroupName=ele.get('ResourceGroupName')
        #     )
        #     authorizeType = ele.get('authorizeType')
        #     namespaceStatus = ele.get('namespaceStatus')
        #     namespaceName = ele.get('namespace')
        #     defaultVisibility = ele.get('defaultVisibility')
        #     autoCreate = ele.get('autoCreate')
        #
        #     Namespace.objects.get_or_create(
        #         authorizeType=authorizeType,
        #         namespaceStatus=namespaceStatus,
        #         namespaceName=namespaceName,
        #         defaultVisibility=defaultVisibility,
        #         autoCreate=autoCreate,
        #         depart_resource=depart_resource
        #     )

        total_data = Namespace.objects.select_related('depart_resource').all()
        response_data_list = []
        for i in total_data:
            defaultVisibility = '私有' if i.defaultVisibility == 'PRIVATE' else '公有'
            authorizeType = i.authorizeType
            namespaceStatus = '正常' if i.namespaceStatus == 'NORMAL' else i.namespaceStatus
            namespaceName = i.namespaceName
            autoCreate = i.autoCreate

            Department = i.depart_resource.Department
            DepartmentName = i.depart_resource.DepartmentName
            ResourceGroup = i.depart_resource.ResourceGroup
            ResourceGroupName = i.depart_resource.ResourceGroupName

            data = {
                'Department': Department,
                'DepartmentName': DepartmentName,
                'ResourceGroup': ResourceGroup,
                'ResourceGroupName': ResourceGroupName,
                'authorizeType': authorizeType,
                'namespaceStatus': namespaceStatus,
                'namespaceName': namespaceName,
                'defaultVisibility': defaultVisibility,
                'autoCreate': autoCreate,
                'region': 'jibei-1'
            }
            response_data_list.append(data)

        # detail_list = Namespace.objects.all()
        # serializer = NamespaceSerializer(data=detail_list, many=True)
        # if serializer.is_valid():
        #     pass
        #
        # return Response(serializer.data, status=200)
        return Response(response_data_list)


class NamespaceConfigModify(APIView):
    def get(self, request):
        data = {
            "value": '160',
            "label": '国网冀北电力有限公司',
            "children": [
                {
                    "value": '1-1',
                    "label": '研发测试平台',
                    "children": [
                        {
                            "value": '1-1-1',
                            "label": '云平台',
                        },
                    ],
                },
                {
                    "value": '1-1',
                    "label": '发展策划部',
                },
                {
                    "value": '1-1',
                    "label": '财务部',
                },
                {
                    "value": '1-1',
                    "label": '安监部、保卫部',
                },
                {
                    "value": '1-1',
                    "label": '设备管理部',
                },
            ],
        }
        return Response(data)
