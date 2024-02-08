from django.urls import path, re_path, include
from rest_framework import routers
from .views import RefreshAppInstance, AppInstanceList
router = routers.DefaultRouter()


urlpatterns = [
    re_path('refresh', RefreshAppInstance.as_view(), name='qweqwipts'),
    re_path('list', AppInstanceList.as_view(), name='qweqwiptsqw1212'),

]
