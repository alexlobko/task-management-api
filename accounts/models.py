from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    deputy = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='deputy_of')
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username