from django.db import models
from accounts.models import CustomUser


class Task(models.Model):
    STATUS_CHOICES = [
        ('Исполнено', 'Исполнено'),
        ('Не исполнено', 'Не исполнено'),
    ]
    content = models.TextField()
    main_executor = models.ForeignKey(CustomUser, related_name='main_tasks', on_delete=models.CASCADE)
    co_executors = models.ManyToManyField(CustomUser, related_name='co_tasks', blank=True)
    deadline = models.DateField(blank=True, null=True)
    regulation = models.ForeignKey('RegulatoryDocument', related_name='tasks_of_regulation', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='Не исполнено')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.content[:30]} до {self.deadline}'


class RegulatoryDocument(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('Протокол', 'Протокол'),
        ('Решение', 'Решение'),
        ('Приказ', 'Приказ'),
        ('Распоряжение', 'Распоряжение'),
    ]
    doc_type = models.CharField(max_length=100, choices=DOCUMENT_TYPE_CHOICES, blank=True, null=True)
    date_approved = models.DateField()
    registration_number = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    # tasks = models.ManyToManyField('Task', related_name='regulatory_documents', blank=True)
    status = models.BooleanField(default=False)

    def update_status(self):
        self.status = all(task.status == 'Исполнено' for task in self.tasks_of_regulation.all())
        self.save()


    def __str__(self):
        return f"{self.doc_type} от {self.date_approved} №{self.registration_number}"


