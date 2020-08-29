# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 22:09
# @Author  : Jackxia
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import  Menu

class MenuSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'url', 'parent', 'icon')
