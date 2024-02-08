# coding=utf-8
import json
from aliyunsdkasapi.ASClient import ASClient
from aliyunsdkasapi.AsapiRequest import AsapiRequest
import datetime

"""

dt = datetime.datetime.fromtimestamp(1605780021000 / 1000)
dt.strftime('%Y-%m-%d %H:%M:%S')
"""


class RepoList(object):
    def __init__(self):
        self.accessKeyId = "DN4"
        self.accessKeySecret = "zSeg"
        self.region = "ji"
        self.endpoint = "httpom.cn/asapi/v3"

    def run(self):
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
        request = AsapiRequest("cr", "2016-06-07", "GetRepoList", self.endpoint)
        # 设置请求方式
        request.set_method("POST")
        request.add_header("x-acs-organizationid", "160")
        # 发起请求，并获取返回
        response = client.do_request(request)

        data_list = []
        repo_data = json.loads(str(response, encoding='utf-8'))
        repos = repo_data.get('data').get('repos')
        # print(len(repos))
        for repo in repos:
            # print(repo)
            gmtModified = repo.get('gmtModified')
            dt = datetime.datetime.fromtimestamp(gmtModified / 1000)
            gmtModified = dt.strftime('%Y-%m-%d %H:%M:%S')
            repo.update({'gmtModified': gmtModified})
            repoNamespace = repo.get('repoNamespace')
            repoName = repo.get('repoName')
            repoDomainList = repo.get('repoDomainList')
            repoDomain = repoDomainList.get('internal')
            repoUrl = '{}/{}/{}'.format(repoDomain, repoNamespace, repoName)
            repo.update({'repoUrl': repoUrl})
            data_list.append(repo)

        return data_list


if __name__ == '__main__':
    aa = RepoList()
    dd = aa.run()
    # for d in dd:
    #     print(d)
