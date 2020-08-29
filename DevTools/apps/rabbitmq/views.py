from .models import Servers, ClusterInfo
from .serializers import RServerSerializer,ClusterSerializer

from rest_framework import viewsets


class RServersViewSet(viewsets.ModelViewSet):
    queryset = Servers.objects.all()  # 指定要序列化的数据
    serializer_class = RServerSerializer  # 指定要使用的序列化类

class ClusterViewSet(viewsets.ModelViewSet):
    queryset = ClusterInfo.objects.all()  # 指定要序列化的数据
    serializer_class = ClusterSerializer  # 指定要使用的序列化类


