from django.contrib import admin

from apis.models import RegulatoryDocument, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'main_executor', 'get_co_executors', 'deadline', 'status')
    list_filter = ('status', 'main_executor')
    search_fields = ('content', 'main_executor__username', 'main_executor__full_name', 'co_executors__username',
                     'co_executors__full_name')

    def get_co_executors(self, obj):
        return ", ".join([user.username for user in obj.co_executors.all()])

    get_co_executors.short_description = 'Co-Executors'


@admin.register(RegulatoryDocument)
class RegulatoryDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'doc_type', 'date_approved', 'registration_number', 'status')
    list_filter = ('status', 'doc_type')
    search_fields = ('full_name', 'registration_number', 'tasks__content')


