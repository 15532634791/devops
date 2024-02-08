from django.urls import path, re_path, include
from rest_framework import routers
router = routers.DefaultRouter()
from .views import ImageRepoView, FileUploadView, ScriptFileList, DeleteScriptFile, RepoImageSync, RepoTagsView

router.register(r'list', ImageRepoView, basename='ImageRepo')

urlpatterns = [
    re_path('upload/', FileUploadView.as_view(), name='file-upload'),
    re_path('script/', ScriptFileList.as_view(), name='file-scripts'),
    re_path('sync/', RepoImageSync.as_view(), name='filewq-scripts'),
    re_path(r'delete/(.*)', DeleteScriptFile.as_view(), name='file-delete'),
    re_path(r'tags/', RepoTagsView.as_view(), name='tags-delete'),

]
urlpatterns += router.urls
