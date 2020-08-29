# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 21:14
# @Author  : Jackxia
from django_filters import rest_framework as filters
from .models import Servers as cmdb_servers

class ServerFilter(filters.FilterSet):
    class Meta:
        server = filters.AllValuesFilter(field_name='hostname', lookup_expr='eq')
        model = cmdb_servers  # 模型名
        fields = {
            'hostname': ['icontains'],
        }


