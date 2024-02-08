from django.urls import path, re_path, include
from rest_framework import routers
from .views import DepartmentResource, DepartmentResourceDetail, NamespaceDepartmentResourceSync,NamespaceConfigModify
router = routers.DefaultRouter()


urlpatterns = [
    re_path('list/', DepartmentResource.as_view(), name='sss-scripts'),
    re_path('detail/', DepartmentResourceDetail.as_view(), name='sss1-scripts'),
    re_path('sync/', NamespaceDepartmentResourceSync.as_view(), name='sss2-scripts'),
    re_path('modify/', NamespaceConfigModify.as_view(), name='sss2-sc2112ripts'),
]
