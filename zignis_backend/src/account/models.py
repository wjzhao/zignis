from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    ROLES = (
        ('developer', u'开发'),
        ('product manager', u'产品'),
        ('test', u'测试'),
    )
    leader = models.ForeignKey('User', null=True, blank=True, on_delete=models.CASCADE, related_name='leader_dev')
    admin_mail = models.ForeignKey('User', null=True, blank=True, on_delete=models.CASCADE, related_name='admin_dev')
    role = models.CharField(max_length=32, default='developer', choices=ROLES)
    mail_list_extend = models.TextField(null=True, blank=True)
    remark = models.CharField(max_length=128, default='', blank=True)

    class Meta:
        verbose_name = u'用户'

    def __str__(self):
        return self.username
