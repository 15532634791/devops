from django.urls import path, re_path, include
from rest_framework import routers
from.views import NetworkTestView, ShellTestView
router = routers.DefaultRouter()


urlpatterns = [
    re_path('network', NetworkTestView.as_view(), name='netwrok'),
    re_path('shell', ShellTestView.as_view(), name='shell'),
]
