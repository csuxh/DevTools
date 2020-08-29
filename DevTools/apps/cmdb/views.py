# from django.views.generic import View
from .models import Servers as cmdb_servers
from .serializers import ServerSerializer
from rest_framework import viewsets
import json
# from rest_framework.decorators import action
# from django.http import JsonResponse
from rest_framework.response import Response

class ServersView(viewsets.ModelViewSet):
    # print('in cmdb')
    queryset  = cmdb_servers.objects.all()
    serializer_class = ServerSerializer
    # pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(self.queryset)
        if request.method == 'GET':
            server_type = request.GET.get('server_type')
            hostname = request.GET.get('name')
            if len(hostname) > 0:
                page = self.paginate_queryset(cmdb_servers.objects.filter(name=hostname))

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)

    # @action(methods=['get', 'post'], detail=False, url_path='user_action')
    # def user_action(self, request, *args, **kwargs):
    #     dd = {"w": "ww", "ee": "ttt"}
    #     return JsonResponse(dd)
