# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 22:27
# @Author  : Jackxia
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import  ClusterInfo,Servers

class RServerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Servers
        fields = ('__all__')

class ClusterSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ClusterInfo
        fields = ('__all__')
