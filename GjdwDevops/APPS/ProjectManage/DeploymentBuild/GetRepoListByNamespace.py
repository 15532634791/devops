#coding=utf-8
import json
from aliyunsdkasapi.ASClient import ASClient
from aliyunsdkasapi.AsapiRequest import AsapiRequest

# 本文提供的API调用样例仅供参考，更多详细API调用方法可参照开发文档中的“快速入门”
#
# # 创建ASClient连接,timeout设置请求超时时间，cert_file设置证书文件，verify是否验证证书
# client = ASClient("hdjbtrn4IJiZRp4V", "DtYy6ZjBImnFpsltFGxs2PDZZuc5Vu", "jibei-1", timeout=1000,
#             cert_file=None,
#             verify=False)
# # 设置身份标识,标识调用来源,无实际作用,可随意设置,必填项
# client.setSdkSource("asapi-5614@asapi-inc.com")
# # ASAPI的Endpoint地址
# endpoint = "http://internal.asapi.jibei-1.ops.sgmc.sgcc.com.cn/asapi/v3"
# # 创建Request
# request = AsapiRequest("cr", "2016-06-07", "GetRepoListByNamespace", endpoint)
# # 设置请求方式
# request.set_method("POST")
# # 授权相关参数
#
# # 接口业务参数设置
# # request.add_body_params("Department", "160")
# request.add_body_params("RepoNamespace", "aliyun")
# # request.add_body_params("ResourceGroup", "191")
# request.add_header("x-acs-organizationId", "160")
# request.add_header("x-acs-resourceGroupId", "191")
# # 设置Headers
# # 部分接口需要在页面headers列表中填写x-acs-organizationId、x-acs-resourceGroupId等组织，资源组信息
#
# # 发起请求，并获取返回
# response = client.do_request(request)
#
# # python2:  print(response)
# print(str(response, encoding='utf-8'))
# import json
# data_test = json.loads(
# str(response, encoding='utf-8')
# )
# print(data_test.get('data').get('repos'))
# for i in data_test.get('data').get('repos'):
#     print(i.get('repoName'))


class RepoListByNamespace(object):
    def __init__(self):
        self.accessKeyId = "DNpVFojiUH9I4J34"
        self.accessKeySecret = "zYNmbTwtZpBMFKPpKdzVn4Ukk3pSeg"
        self.region = "jibei-1"
        self.endpoint = "http://internal.asapi.jibei-1.ops.sgmc.sgcc.com.cn/asapi/v3"

    def run(self, namespace):
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
        request = AsapiRequest("cr", "2016-06-07", "GetRepoListByNamespace", self.endpoint)
        # 设置请求方式
        request.set_method("POST")
        # 接口业务参数设置
        request.add_body_params("RepoNamespace", namespace)
        request.add_header("x-acs-organizationId", "160")
        request.add_header("x-acs-resourceGroupId", "191")
        # 发起请求，并获取返回
        response = client.do_request(request)

        # python2:  print(response)
        # print(str(response, encoding='utf-8'))
        temp_data = json.loads(str(response, encoding='utf-8'))
        temp_data = temp_data.get('data').get('repos')
        # print(temp_data)
        if temp_data:
            handle_data = []
            for tmp in temp_data:
                # print(tmp)
                tmp_dict = {'label': tmp.get('repoName'), 'value': tmp.get('repoName')}
                # print(tmp_dict)
                handle_data.append(tmp_dict)
            # print(handle_data)
            return handle_data
        else:
            return []


if __name__ == '__main__':
    a = RepoListByNamespace()
    a.run('aliyun')
    # print(a.run('aliyun'))