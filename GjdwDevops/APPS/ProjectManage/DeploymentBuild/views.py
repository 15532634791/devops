import datetime
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import DeployBuildModel
from .serializers import DeployBuildFileSerializer, DeployBuildModelSerializer
from .GetRepoListByNamespace import RepoListByNamespace
import subprocess
from pathlib import Path


class FileUploadView(APIView):
    """
    文件上传
    """
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        file_serializer = DeployBuildFileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response({"status": 'success'}, status=None)
        else:
            return Response(file_serializer.errors, status=None)


class DeployBuildView(APIView):

    @classmethod
    def system_command(cls, command):
        # 调用linux系统命令
        shell = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = shell.communicate()
        try:
            return stdout.decode("utf8"), stderr.decode("utf8"), shell.returncode
        except Exception as e:
            return stdout.decode("gbk"), stderr.decode("gbk"), shell.returncode

    def wrap_text(self, text, max_length):

        docker_ps_status = True

        docker_ps_list = [
            "CONTAINER", "IMAGE", "COMMAND", "CREATED", "STATUS", "PORTS", "NAMES"
        ]
        for field in docker_ps_list:
            if field not in text:
                docker_ps_status = False

        if docker_ps_status:
            return text

        wrapped_text = ''
        while len(text) > max_length:
            wrapped_text += text[:max_length] + '\n'
            text = text[max_length:]
        wrapped_text += text
        return wrapped_text

    @staticmethod
    def command_message(command, correct_output, error_output, return_code):
        message = """_____________________________________________________________________________________________________________________________________________
            
            执行命令: 
            {}
            正确输出:
            {}
            错误输出:
            {}
            返回码:
            {}
            """.format(
            command, correct_output, error_output, return_code
        )
        message = message.replace(
            '                    ', ''
        ).replace(
            '            ', ''
        ).replace(
            '                ', ''
        )
        return message

    def get(self, request):

        deploy_build_list = DeployBuildModel.objects.all()
        serializer = DeployBuildModelSerializer(instance=deploy_build_list, many=True)
        return Response(serializer.data)

    def post(self, request):

        # print(request.data)
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        deploy_data = request.data
        multiple_command_connectors = [';', '&&', '||', ">>", "<", ">", "<<", '|']
        build_command = deploy_data.get('jarBuildCommand')

        # 命令校验
        build_command = [command for command in build_command.split('\n') if command]

        execute_command_output_list = list()
        check_code = 0
        for command in build_command:

            if not command.startswith('docker'):
                check_code = 1
                message = self.command_message(
                    command,
                    "本次构建没有执行命令，只显示错误命令",
                    "只允许执行docker命令",
                    check_code
                )

                execute_command_output_list.append(message)

            for connector in multiple_command_connectors:
                if connector in command:
                    # print("存在特殊命令连接符：;  &&  ||  >>  <  >  << | ")
                    check_code = 1
                    message = self.command_message(
                        command,
                        "本次构建没有执行命令，只显示错误命令",
                        "存在特殊命令连接符：;  &&  ||  >>  <  >  << | ",
                        check_code
                    )

                    execute_command_output_list.append(message)

                    continue

        execute_command_code = 0
        if check_code == 0:
            # print('命令检测正常')
            absolute_path_command = "cd {} && {}".format(
                base_dir, command
            )

            for command in build_command:
                # stdout, stderr, return_code = self.system_command(absolute_path_command)
                stdout, stderr, return_code = self.system_command(command)

                stdout = self.wrap_text(stdout, 140)
                stderr = self.wrap_text(stderr, 140)

                message = self.command_message(
                    command, stdout, stderr, return_code
                )

                execute_command_output_list.append(message)

                if return_code != 0:
                    execute_command_code = 1

        execute_command_output = ''.join(execute_command_output_list)

        build_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        deploy_data['jarBuildTime'] = build_time

        jarBuildName = deploy_data.get('jarBuildName')
        jarBuildNameSpace = deploy_data.get('jarBuildNameSpace')
        jarBuildRepo = deploy_data.get('jarBuildRepo')
        jarBuildVersion = deploy_data.get('jarBuildVersion')
        jarBuildCommand = deploy_data.get('jarBuildCommand')
        jarBuildImageAddress = '{}/{}/{}:{}'.format(
            "cr.registry.jibei-1.res.sgmc.com.cn",
            jarBuildNameSpace,
            jarBuildRepo,
            jarBuildVersion
        )
        deploy_data['jarBuildImageAddress'] = jarBuildImageAddress
        #
        upload_dir = '{}_{}_{}_{}'.format(
            jarBuildName, jarBuildNameSpace, jarBuildRepo, jarBuildVersion
        )

        media_path = os.path.join(
            base_dir,
            'Media',
            'DeployBuild'
        )
        storage_path = os.path.join(media_path, upload_dir)
        # print(storage_path)

        jarBuildStatus = '成功' if check_code == 0 and execute_command_code == 0 else '失败'
        deploy_data['jarBuildCommandStdout'] = execute_command_output
        deploy_data['jarBuildStatus'] = jarBuildStatus
        deploy_data['jarBuildUser'] = 'wangze'
        #
        if jarBuildStatus != '成功' or execute_command_code != 0:
            deploy_data['jarBuildImageAddress'] = ''
        DeployBuildModel.objects.get_or_create(**deploy_data)

        # print(command_stdout)
        return Response()


class GetRepoByNamespace(APIView):

    def get(self, request):
        param_value = request.query_params.get('namespace')
        # repo_list = RepoListByNamespace()
        # repo_list_data = repo_list.run(param_value)
        # return Response(repo_list_data)

        data = [
            {'label': 'java8-gzg', 'value': 'java8-gzg'},
            {'label': 'bpm-web', 'value': 'bpm-web'},
            {'label': 'ydpc-athena-out', 'value': 'ydpc-athena-out'},
            {'label': 'test117', 'value': 'test117'},
            {'label': 'openresty', 'value': 'openresty'}
        ]

        return Response(data)
        # return Response(repo_list_data)


class GetBuildName(APIView):
    def get(self, request):

        param_value = request.query_params.get('query')
        deploy_build = DeployBuildModel.objects.filter(jarBuildName=param_value)

        if not deploy_build:
            data = {'message': 'BuildNameNotExists'}
        else:
            data = {'message': 'BuildNameExists'}
        return Response(data)
