#coding=utf-8
import json
import datetime
from aliyunsdkasapi.ASClient import ASClient
from aliyunsdkasapi.AsapiRequest import AsapiRequest


class RepoTags(object):
    def __init__(self):
        self.accessKeyId = ""
        self.accessKeySecret = ""
        self.region = "j"
        self.endpoint = "http://iom.cn/asapi/v3"

    @staticmethod
    def convert_size(size):
        """将大小转换为最佳单位"""
        print(size)
        if size:
            units = ['bytes', 'KB', 'MB', 'GB', 'TB']
            index = 0
            while size >= 1024 and index < len(units) - 1:
                size /= 1024
                index += 1
            return f"{size:.2f} {units[index]}"
        else:
            return '0bytes'

    def run(self, RepoName=None, RepoNamespace=None):
        client = ASClient(
            self.accessKeyId,
            self.accessKeySecret,
            self.region,
            timeout=1000,
            cert_file=None,
            verify=False
        )
        # 设置身份标识,标识调用来源,无实际作用,可随意设置,必填项
        client.setSdkSource("asapi-9307@asapi-inc.com")
        # 创建Request
        request = AsapiRequest("cr", "2016-06-07", "GetRepoTags", self.endpoint)
        # 设置请求方式
        request.set_method("POST")
        # 接口业务参数设置
        # request.add_body_params("Department", "160")
        # request.add_body_params("RepoName", "nginx")
        request.add_body_params("RepoName", RepoName)
        # request.add_body_params("RepoNamespace", "yptcwdzhcs")
        request.add_body_params("RepoNamespace", RepoNamespace)
        # request.add_body_params("ResourceGroup", "191")
        request.add_header("x-acs-organizationid", "160")
        # 发起请求，并获取返回
        response = client.do_request(request)

        # python2:  print(response)
        # print(str(response, encoding='utf-8'))
        json_data = json.loads(str(response, encoding='utf-8'))
        # print(json_data)
        try:
            tags = json_data.get('data').get('tags')
        except AttributeError:
            return []
        # print(tags)
        data_list = []
        if tags:
            for tag in tags:
                # print(tag)
                imageCreate = tag.get('imageCreate')
                dt = datetime.datetime.fromtimestamp(imageCreate / 1000)
                imageCreate = dt.strftime('%Y-%m-%d %H:%M:%S')
                tag.update({'imageCreate': imageCreate})

                imageUpdate = tag.get('imageUpdate')
                dt = datetime.datetime.fromtimestamp(imageUpdate / 1000)
                imageUpdate = dt.strftime('%Y-%m-%d %H:%M:%S')
                tag.update({'imageUpdate': imageUpdate})

                imageSize = tag.get('imageSize')
                imageSize = self.convert_size(imageSize)
                tag.update({'imageSize': imageSize})

                data_list.append(tag)
            return data_list

        return []


if __name__ == '__main__':
    aa = RepoTags()
    aa.run(RepoName="nginx", RepoNamespace="yptcwdzhcs")
