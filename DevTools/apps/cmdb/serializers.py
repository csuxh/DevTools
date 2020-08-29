# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 17:47
# @Author  : Jackxia
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import  Servers

class ServerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Servers
        fields = ('__all__')


    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Servers.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('name', instance.title)
    #     instance.code = validated_data.get('ip1', instance.code)
    #     instance.linenos = validated_data.get('in_service', instance.linenos)
    #     instance.language = validated_data.get('app_support', instance.language)
    #     instance.style = validated_data.get('business_contact', instance.style)
    #     instance.save()
    #     return instance
