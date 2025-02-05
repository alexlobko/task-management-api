from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html

from apis.models import RegulatoryDocument, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'main_executor', 'get_co_executors', 'regulation' , 'deadline', 'status_display')
    list_filter = ('content', 'main_executor', 'co_executors__full_name', 'deadline', 'regulation', 'status')
    search_fields = ('content', 'main_executor__username', 'main_executor__full_name', 'regulation', 'co_executors__username',
                     'co_executors__full_name')
    filter_horizontal = ('co_executors',)

    def get_co_executors(self, obj):
        return ", ".join([user.full_name for user in obj.co_executors.all()])

    get_co_executors.short_description = 'Co-Executors'

    # def get_regulatory_documents(self, obj):
    #     return ", ".join([doc.__str__() for doc in obj.regulation.all()])
    #
    # get_regulatory_documents.short_description = 'Regulatory Documents'
    def status_display(self, obj):
        if obj.status == 'Не исполнено':
            if obj.deadline:
                time_until_due = obj.deadline - timezone.now().date()
                if time_until_due.days < 0:
                    return format_html('<span style="color:red;">Не выполнена (Просрочено)</span>')
                elif time_until_due.days < 3:
                    return format_html('<span style="color:pink;">Не выполнена (Истекает скоро)</span>')
            return 'Не исполнено'
        elif obj.status == 'Исполнено':
            return format_html('<span style="color:green;">Выполнена</span>')
        else:
            return obj.status

    status_display.short_description = 'Статус'

@admin.register(RegulatoryDocument)
class RegulatoryDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'doc_type', 'date_approved', 'registration_number', 'get_tasks', 'status')
    list_filter = ('doc_type', 'status', 'registration_number')
    search_fields = ('full_name', 'registration_number', 'tasks__content')

    def get_tasks(self, obj):
        return " | ".join([f'{task.__str__()} - {task.status}' for task in obj.tasks_of_regulation.all()])

    get_tasks.short_description = 'Tasks'
