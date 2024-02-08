# -*- coding:utf-8 -*-
import json
from aliyunsdkasapi.ASClient import ASClient
from aliyunsdkasapi.AsapiRequest import AsapiRequest


class NamespaceDetail(object):

    def __init__(self):
        self.accessKeyId = "D9I4J34"
        self.accessKeySecret = "pSeg"
        self.region = "jib1"
        self.endpoint = "httpasapi/v3"

    def run(self, org_id, resource_set_id, namespace):
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

        request = AsapiRequest("cr", "2016-06-07", "GetNamespace", self.endpoint)
        # 设置请求方式
        request.set_method("POST")
        request.add_body_params("Namespace", namespace)

        request.add_header("x-acs-organizationId", str(org_id))
        request.add_header("x-acs-resourceGroupId", str(resource_set_id))

        # 发起请求，并获取返回
        response = client.do_request(request)

        # python2:  print(response)
        # print(str(response, encoding='utf-8'))
        namespace_data = json.loads(str(response, encoding='utf-8'))
        if namespace_data.get('asapiSuccess'):
            ret_data = namespace_data.get('data').get('namespace')
            # print(ret_data)
            return ret_data
        else:
            ret_data = {}
            return ret_data


class NamespaceList(object):
    def __init__(self):
        self.accessKeyId = "DNpVFojiUH9I4J34"
        self.accessKeySecret = "zYNmbTwtZpBMFKPpKdzVn4Ukk3pSeg"
        self.region = "jibei-1"
        self.endpoint = "http://internal.asapi.jibei-1.ops.sgmc.sgcc.com.cn/asapi/v3"
        self.namespace_detail = NamespaceDetail()

    def namespace(self):
        client = ASClient(
            self.accessKeyId,
            self.accessKeySecret,
            self.region,
            timeout=1000,
            cert_file=None,
            verify=False
        )
        client.setSdkSource("GetNamespaceList")
        # 创建Request
        request = AsapiRequest("cr", "2016-06-07", "GetNamespaceList", self.endpoint)
        # 设置请求方式
        request.set_method("POST")

        # 设置Headers
        # 部分接口需要在页面headers列表中填写x-acs-organizationId、x-acs-resourceGroupId等组织，资源组信息
        request.add_header("x-acs-organizationid", "160")
        # 发起请求，并获取返回
        response = client.do_request(request)
        data = json.loads(response.decode('utf-8'))
        # print(data.get('data').get('namespaces'))

        namespaces_list = data.get('data').get('namespaces')
        return namespaces_list

    def get_department_resource(self):
        dep_res = list()
        data = self.namespace()
        for i in data:
            # print(i)
            Department = i.get('Department')
            DepartmentName = i.get('DepartmentName')
            ResourceGroup = i.get('ResourceGroup')
            ResourceGroupName = i.get('ResourceGroupName')
            # namespace_detail_data = self.namespace_detail.run(Department, ResourceGroup)
            element = {
                'Department': Department, 'DepartmentName': DepartmentName,
                'ResourceGroup': ResourceGroup, 'ResourceGroupName': ResourceGroupName
            }
            # element.update(namespace_detail_data)
            if element not in dep_res:
                dep_res.append(element)
                print(element)
        return dep_res

    def get_department_resource_detail(self):
        dep_res = list()
        data = self.namespace()
        for i in data:
            # print(i)
            Department = i.get('Department')
            DepartmentName = i.get('DepartmentName')
            ResourceGroup = i.get('ResourceGroup')
            ResourceGroupName = i.get('ResourceGroupName')
            namespace = i.get('namespace')
            namespace_detail_data = self.namespace_detail.run(Department, ResourceGroup,namespace)
            element = {
                'Department': Department, 'DepartmentName': DepartmentName,
                'ResourceGroup': ResourceGroup, 'ResourceGroupName': ResourceGroupName
            }
            element.update(namespace_detail_data)
            # print(element)
            if element not in dep_res:
                dep_res.append(element)
                print(element)
        return dep_res


class CreateNamespace(object):
    def __init__(self):
        self.accessKeyId = "hdjbtrn4IJiZRp4V"
        self.accessKeySecret = "DtYy6ZjBImnFpsltFGxs2PDZZuc5Vu"
        self.region = "jibei-1"
        self.endpoint = "http://internal.asapi.jibei-1.ops.sgmc.sgcc.com.cn/asapi/v3"

    def run(self, org_value=None, resource_set_value=None, region_value=None, namespace_value=None):
        client = ASClient(
            self.accessKeyId,
            self.accessKeySecret,
            self.region,
            timeout=1000,
            cert_file=None,
            verify=False
        )
        client.setSdkSource("CreateNamespace")
        # 创建Request。
        request = AsapiRequest("cr", "2016-06-07", "CreateNamespace", self.endpoint)
        # 设置请求方式。
        request.set_method("POST")

        # 接口业务参数设置。
        request.add_body_params("NamespaceName", namespace_value)
        request.add_body_params("Department", org_value)
        request.add_body_params("ResourceGroup", resource_set_value)

        # request.add_body_params("X-acs-body",
        #                         '{"namespace":{"NamespaceName":"%s","haApsaraStack":"false","Department":%s,"Language":"zh","namespace":%s,"arch":"x86_64","RegionId":"%s","ResourceGroup":%s}}'%(
        #                             namespace_value,org_value,namespace_value,region_value, resource_set_value
        #                         ))
        # request.add_body_params("NamespaceName", "ds081123")
        # request.add_body_params("Department", "160")
        # request.add_body_params("ResourceGroup", "191")
        #
        request.add_body_params("X-acs-body",
                                '{"namespace":{"NamespaceName":"%s","haApsaraStack":"false","Department":%s,"Language":"zh","namespace":"%s","arch":"x86_64","RegionId":"%s","ResourceGroup":%s}}' %(namespace_value, org_value, namespace_value,region_value,resource_set_value))

        # 设置Headers。
        # request.add_header("x-acs-resourcegroupid", "2");
        # request.add_header("x-acs-organizationid", "3");
        # 发起请求，并获取返回。
        response = client.do_request(request)

        # 打印响应结果，python2:  print(response)。
        print(str(response, encoding='utf-8'))


if __name__ == '__main__':
    # des = NamespaceList()
    # des.get_department_resource_detail()

    ns = CreateNamespace()
    # ns.run(org_value='160', resource_set_value='191', region_value='jibei-1', namespace_value='ds08222')
