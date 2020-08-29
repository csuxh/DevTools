from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from cmdb import views as cmdb_views
from rabbitmq import views as rabbitmq_views
from dashboard import views as dashboard_views

router = DefaultRouter()
# 注册路由

router.register(r'rabbitmq/serverlist', rabbitmq_views.RServersViewSet)
router.register(r'rabbitmq/clusters', rabbitmq_views.ClusterViewSet)
router.register(r'dashboard/menues', dashboard_views.MenueViewSet)
router.register(r'cmdb/servers', cmdb_views.ServersView)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'api/login', dashboard_views.Login.as_view(), name='login'),
    url('api/', include(router.urls))
]
