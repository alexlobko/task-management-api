from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Task, RegulatoryDocument

@receiver(post_save, sender=Task)
def update_document_status_on_task_save(sender, instance, **kwargs):
    if instance.regulation:
        instance.regulation.update_status()

# @receiver(m2m_changed, sender=RegulatoryDocument.tasks_of_regulation.through)
# def update_document_status_on_m2m_change(sender, instance, action, **kwargs):
#     if action in ["post_add", "post_remove", "post_clear"]:
#         instance.update_status()
