from django.db import models
import uuid
# Create your models here.
class Servers(models.Model):
    server_id = models.CharField(verbose_name='server_id', max_length=50, blank=True)
    name = models.CharField(verbose_name='name', max_length=50, blank=True)
    server_type = models.CharField(verbose_name='server_type', max_length=20, blank=True)
    hostname = models.CharField(verbose_name='hostname', max_length=50, blank=True,null=True)
    ip1 = models.CharField(verbose_name='ip', max_length=50, blank=True)
    ip2 = models.CharField(verbose_name='ip', max_length=50, blank=True)
    in_service = models.CharField(verbose_name='in_service', max_length=10, blank=True)
    service_level = models.CharField(verbose_name='service_level', max_length=40, blank=True)
    site = models.CharField(verbose_name='site', max_length=20, blank=True)
    location = models.CharField(verbose_name='location', max_length=100, blank=True)
    os = models.CharField(verbose_name='os', max_length=50, blank=True)
    cpu = models.CharField(verbose_name='cpu', max_length=5, blank=True)
    mem = models.CharField(verbose_name='mem', max_length=5, blank=True)
    platform_support = models.CharField(verbose_name='platform_support', max_length=100, blank=True)
    app_support = models.CharField(verbose_name='app_support', max_length=100, blank=True)
    disk = models.CharField(verbose_name='disk', max_length=10, blank=True)
    business_contact = models.CharField(verbose_name='business_contact', max_length=100, blank=True)
    it_contact = models.CharField(verbose_name='it_contact', max_length=100, blank=True)
    modify_time = models.CharField(verbose_name='modify_time', max_length=20, blank=True)
    add_time = models.DateTimeField(auto_now_add=True, blank=True)
    class Meta:
        ordering = ('server_id',)