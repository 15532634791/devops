from django.urls import path, re_path, include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import DeployBuildView, FileUploadView, GetRepoByNamespace, GetBuildName


urlpatterns = [
    re_path('deploy/', DeployBuildView.as_view(), name='sqw12ss-scripts'),
    re_path('upload/', FileUploadView.as_view(), name='sq2112ss-scr12ipts'),
    re_path('repo/', GetRepoByNamespace.as_view()),
    re_path('query/', GetBuildName.as_view())
]
