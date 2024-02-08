# -*- coding:utf8 -*-
import os
import json


class GetAppInstanceList(object):

    def app_instance(self):
        with open(r'D:\temp\20231016\GjdwDevops\APPS\ProjectManage\AppInstance\获取应用列表.json', 'r') as file:
            data = file.read()
            data = json.loads(data)

            application_list = data.get('ApplicationList').get("Application")
            return application_list
