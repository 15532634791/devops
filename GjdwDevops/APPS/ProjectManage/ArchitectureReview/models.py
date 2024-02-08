from django.db import models


class ArchitectureReviewModel(models.Model):
    """
    项目架构评审表
    与 项目架构评审详细信息表 为一对一关系
    """
    system_name = models.CharField(max_length=255, help_text='业务系统名称')
    project_name = models.CharField(max_length=255, help_text='项目名称')
    framework_type = models.CharField(null=True, blank=True, max_length=50, help_text='架构类型')
    project_type = models.CharField(null=True, blank=True, max_length=50, help_text='项目类别')
    buz_org = models.CharField(null=True, blank=True, max_length=100, help_text='业务部门')

    class Meta:
        db_table = 'architecture_review'


class ArchitectureReviewModelDetail(models.Model):
    """
    项目架构评审详细信息表
    """
    pro_arc_rev = models.OneToOneField(to='ArchitectureReviewModel', to_field='id', on_delete=models.CASCADE, help_text='一对一关系')
    first_submit_time = models.DateTimeField(null=True, blank=True, help_text='首次提报时间')
    first_approval_time = models.DateTimeField(null=True, blank=True, help_text='首次审批时间')
    submit_count = models.IntegerField(null=True, blank=True, help_text='提报次数')
    last_submit_time = models.DateTimeField(null=True, blank=True, help_text='最后提报时间')
    approval_pass_time = models.DateTimeField(null=True, blank=True, help_text='审批通过时间')
    approval_opinion = models.CharField(null=True, blank=True, max_length=50, help_text='审批意见')
    is_cloud = models.CharField(null=True, blank=True, max_length=50, help_text='是否上云')
    cloud_time = models.DateTimeField(null=True, blank=True, help_text='上云时间')
    deployment_time = models.DateTimeField(null=True, blank=True, help_text='实施部署时间')
    owner_org_name = models.CharField(null=True, blank=True, max_length=255, help_text='建设单位')
    owner_user_name = models.CharField(null=True, blank=True, max_length=50, help_text='建设单位负责人')
    owner_user_tel = models.CharField(null=True, blank=True, max_length=20, help_text='建设单位负责人电话')
    owner_user_email = models.CharField(null=True, blank=True, max_length=100, help_text='建设单位负责人邮箱')
    buz_org_user_name = models.CharField(null=True, blank=True, max_length=100, help_text='业务部门负责人')
    buz_org_user_tel = models.CharField(null=True, blank=True, max_length=100, help_text='业务部门负责人电话')
    buz_org_user_mail = models.CharField(null=True, blank=True, max_length=100, help_text='业务部门负责人邮箱')
    cons_org_name = models.CharField(null=True, blank=True, max_length=100, help_text='承建单位')
    cons_user_name = models.CharField(null=True, blank=True, max_length=100, help_text='承建单位负责人')
    cons_user_tel = models.CharField(null=True, blank=True, max_length=100, help_text='承建单位电话')
    cons_user_mail = models.CharField(null=True, blank=True, max_length=100, help_text='承建单位邮箱')

    class Meta:
        db_table = 'architecture_review_detail'


from django.db import models



