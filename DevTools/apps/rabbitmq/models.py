from django.db import models

# Create your models here.
class Servers(models.Model):
    server_id = models.CharField(verbose_name='env', max_length=10)
    env = models.CharField(verbose_name='env', max_length=10)
    hostsname = models.CharField(verbose_name='hostname', max_length=50)
    ip = models.CharField(verbose_name='ip', max_length=50)
    clustername = models.CharField(verbose_name='hostname', max_length=20)
    clusterid = models.CharField(verbose_name='cluster_id', max_length=10)
    disk = models.CharField(verbose_name='disk', max_length=30)
    memory = models.CharField(verbose_name='memory', max_length=30)
    cpu = models.CharField(verbose_name='cpu', max_length=30)
    version = models.CharField(verbose_name='version', max_length=30)
    port = models.IntegerField(verbose_name='port')
    # add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('server_id',)

class ClusterInfo(models.Model):
    clusterid = models.CharField(verbose_name='env', max_length=10)
    description = models.CharField(verbose_name='hostname', max_length=100)
    manageport = models.IntegerField(verbose_name='sentinelport')
    # add_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('clusterid',)