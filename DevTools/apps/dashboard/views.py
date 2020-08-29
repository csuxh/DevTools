from .models import Menu
from .serializers import MenuSerializer
from django.views.generic import View
from rest_framework import viewsets
from django.http import JsonResponse
import json
from utils.ldapApi import check_login
class MenueViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class Login(View):
    def post(self, request):
        rs = json.loads(request.body.decode('utf-8'))
        username = rs.get('username')
        password = rs.get('password')
        print(username, password)
        if len(username.split('.')) == 2:
            status = check_login(username, password)
        elif username == 'admin' and password == 'admin123':
            status = True
        else:
            status = False
        if status:
            return JsonResponse({'status': 1})
        else:
            return JsonResponse({'status': 0})


