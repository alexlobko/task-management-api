from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models




class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    deputy = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='deputy_of')
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.full_name

    def delete(self, *args, **kwargs):
        from apis.models import Task
        deputy = self.deputy
        users_to_update = CustomUser.objects.filter(deputy=self)

        if deputy:
            for user in users_to_update:
                user.deputy = deputy
                user.save()

            Task.objects.filter(main_executor=self).update(main_executor=deputy)
            for task in Task.objects.filter(co_executors=self):
                task.co_executors.remove(self)
                task.co_executors.add(deputy)
        super().delete(*args, **kwargs)