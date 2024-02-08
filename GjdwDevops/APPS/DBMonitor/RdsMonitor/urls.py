from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('resource', views.RdsDatabaseResourceInfoView)
router.register('instance', views.RdsInstanceInfoView)
router.register('monitor', views.RdsDatabaseMonitorView)

urlpatterns = []
urlpatterns += router.urls
