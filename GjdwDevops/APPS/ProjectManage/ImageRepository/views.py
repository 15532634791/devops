from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import ImageRepoModel
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
import os
from datetime import datetime
from .GetRepoList import RepoList
from .models import ImageRepoModel
from .GetRepoTags import RepoTags


class RepoImageSync(APIView):
    def get(self, requests):
        repo_list = RepoList()
        repo_list = repo_list.run()
        for repo in repo_list:
            print(repo)
            repo_data = {
                'repoId': repo.get('repoId'),
                'repoName': repo.get('repoName'),
                'repoNamespace': repo.get('repoNamespace'),
                'repoStatus': repo.get('repoStatus'),
                'repoType': repo.get('repoType'),
                'repoAuthorizeType': repo.get('repoAuthorizeType'),
                'repoUrl': repo.get('repoUrl'),
                'gmtModified': repo.get('gmtModified'),
            }
            ImageRepoModel.objects.get_or_create(**repo_data)

        return Response({'sync_status': 'success'}, status=200)


class ImageRepoSerializers(serializers.ModelSerializer):

    class Meta:
        model = ImageRepoModel
        fields = '__all__'
        # exclude = ['pub_date']


class ImageRepoView(ModelViewSet):
    queryset = ImageRepoModel.objects.all()
    serializer_class = ImageRepoSerializers


class RepoTagsView(APIView):
    def get(self, request):
        RepoName = request.query_params.get('RepoName')
        RepoNamespace = request.query_params.get('RepoNamespace')
        print(RepoNamespace, RepoName)

        repo_tags = RepoTags()
        data = repo_tags.run(RepoName=RepoName, RepoNamespace=RepoNamespace)

        return Response(data)



class FileUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response("文件上传成功", status=None)
        else:
            return Response(file_serializer.errors, status=None)


class ScriptFileList(APIView):

    @staticmethod
    def convert_size(size):
        """将大小转换为最佳单位"""
        units = ['bytes', 'KB', 'MB', 'GB', 'TB']
        index = 0
        while size >= 1024 and index < len(units) - 1:
            size /= 1024
            index += 1
        return f"{size:.2f} {units[index]}"

    def get(self, request):

        file_total_list = list()
        root_locate = 'Media/uploads'
        file_locate_list = os.listdir(root_locate)
        for locate in file_locate_list:

            file_name = os.path.join(root_locate, locate)
            file_size = os.path.getsize(file_name)
            file_size = self.convert_size(file_size)
            create_time = os.path.getctime(file_name)
            datetime_obj = datetime.fromtimestamp(create_time)
            formatted_date = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

            data = {
                'uploader': 'wangze',
                'file_name': locate,
                'file_size': file_size,
                'create_time': formatted_date,
                'version': 'v1',
                'label': '20230201'
            }
            file_total_list.append(data)

        return Response(file_total_list)


class DeleteScriptFile(APIView):

    def get(self, request, file_name):
        root_locate = 'Media/uploads/'
        file_name = os.path.join(root_locate, file_name)
        print(file_name)
        try:
            os.remove(file_name)
        except FileNotFoundError:
            ...
        return Response({
            'name': '{}\t 已经删除'.format(file_name)
        })
