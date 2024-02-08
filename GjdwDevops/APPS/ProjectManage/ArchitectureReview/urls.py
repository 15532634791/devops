from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('api', views.ArchitectureReviewModelView, basename='api')
router.register('api01', views.ArchitectureReviewModelViewDetail, basename='api01')
# from .views import AccountViewSet, ArchitectureReviewViewSet

# router = DefaultRouter()
# router.register(r'accounts', AccountViewSet)
# router.register(r'test', ArchitectureReviewViewSet)

urlpatterns = []
urlpatterns += router.urls
