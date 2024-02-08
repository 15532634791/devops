import time
import ping3
import telnetlib
import subprocess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class NetworkTestView(APIView):
    permission_classes = [AllowAny]

    @classmethod
    def system_command(cls, command):

        """
        执行系统命令
        :param command: 命令
        :return: 输出结果，报错，执行状态
        :param command:
        :return:
        """

        shell = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = shell.communicate()
        try:
            return stdout.decode("utf8"), stderr.decode("utf8"), shell.returncode
        except Exception:
            return stdout.decode("gbk"), stderr.decode("gbk"), shell.returncode

    def ping_tools(self, ip):

        stdout, stderr, code = self.system_command('ping {}'.format(ip))
        print(stdout, stderr, code)
        return stdout

        try:
            response_time = ping3.ping(dest_addr=ip, timeout=1)
            if response_time is not None:
                print("Ping successful. Response time:", response_time)
                # output = ping3.verbose_ping(ip, count=5)
                return f"ping {ip} success"
            else:
                print("Ping failed.")
        except Exception as e:
            return f"error {e}"

    def telnet_tools(self, ip, port):
        try:
            tn = telnetlib.Telnet(ip, port, timeout=1)
            tn.close()
            return f"Telnet connection to {ip}:{port} successful."

        except ConnectionRefusedError:
            return f"Connection refused: Unable to connect to {ip}:{port}."
        except TimeoutError:
            return f"Connection timeout: Unable to connect to {ip}:{port}."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def get(self, request):
        return Response({"status": "success"})

    def post(self, request):
        data = request.data
        source_ip = data.get('sourceIp')
        destination_ip = data.get('destinationIp')
        port = data.get('port')

        handle_data = {
            "source_ping": self.ping_tools(source_ip),
            "destination_ping": self.ping_tools(destination_ip),
            'telnet': self.telnet_tools(ip=destination_ip, port=port)
        }

        return Response(handle_data)


class ShellTestView(APIView):
    permission_classes = [AllowAny]

    @classmethod
    def system_command(cls, command):

        """
        执行系统命令
        :param command: 命令
        :return: 输出结果，报错，执行状态
        :param command:
        :return:
        """

        shell = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        stdout, stderr = shell.communicate()
        try:
            return stdout.decode("utf8"), stderr.decode("utf8"), shell.returncode
        except Exception:
            return stdout.decode("gbk"), stderr.decode("gbk"), shell.returncode

    def post(self, request):
        print(request.data)
        command_list = [
            command for command in request.data.get('shellCommand').split('\n') if command
        ]
        print(command_list)

        command_output = []

        for command in command_list:
            stdout, stderr, code = self.system_command(command)
            print(stdout, stderr, code)
            command_opt = stdout if stdout else stderr

            data = {'command': command, 'output': command_opt}
            command_output.append(
                data
            )
        print(command_output)
        return Response(command_output)
