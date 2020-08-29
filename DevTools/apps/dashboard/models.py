from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(verbose_name=u'菜单名称', max_length=30)
    permissions = models.CharField(verbose_name=u"权限", max_length=50)
    url = models.CharField(verbose_name=u'链接index', max_length=100)
    type = models.SmallIntegerField(verbose_name=u'菜单类型', choices=((0, u'菜单'), (1, u'按钮')))
    parent = models.CharField(verbose_name=u'父菜单',max_length=30, default='')
    icon = models.CharField(max_length=100, verbose_name='图标', default='menu-icon fa fa-pencil-square-o')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'菜单'
        verbose_name_plural = verbose_name
