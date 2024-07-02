from django.test import TestCase
from django.utils import timezone

from accounts.models import CustomUser
from .models import Task, RegulatoryDocument


class BaseTestCase(TestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(username='user1')
        self.user2 = CustomUser.objects.create(username='user2')
        self.regulatory_doc = RegulatoryDocument.objects.create(
            doc_type='Протокол',
            date_approved=timezone.now().date(),
            registration_number='123',
            full_name='Test Regulatory Document'
        )
        self.task1 = Task.objects.create(
            content='Task 1',
            main_executor=self.user1,
            deadline=timezone.now().date(),
            regulation=self.regulatory_doc,
            status='Исполнено'
        )
        self.task2 = Task.objects.create(
            content='Task 2',
            main_executor=self.user2,
            deadline=timezone.now().date(),
            regulation=self.regulatory_doc,
            status='Не исполнено'
        )


class TaskTestCase(BaseTestCase):
    def test_task_creation(self):
        self.assertEqual(self.task1.content, 'Task 1')
        self.assertEqual(self.task1.main_executor, self.user1)
        self.assertEqual(self.task1.co_executors.count(), 0)
        self.assertEqual(self.task1.deadline, timezone.now().date())
        self.assertEqual(self.task1.regulation, self.regulatory_doc)
        self.assertEqual(self.task1.status, 'Исполнено')

    def test_task_update(self):
        self.task1.status = 'Не исполнено'
        self.task1.save()
        self.assertEqual(self.task1.status, 'Не исполнено')

    def test_task_update_with_refresh_from_db(self):
        self.task1.status = 'Не исполнено'
        self.task1.save()
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, 'Не исполнено')


class RegulatoryDocumentTestCase(BaseTestCase):
    def test_regulatory_document_creation(self):
        self.assertEqual(self.regulatory_doc.doc_type, 'Протокол')
        self.assertEqual(self.regulatory_doc.date_approved, timezone.now().date())
        self.assertEqual(self.regulatory_doc.registration_number, '123')
        self.assertEqual(self.regulatory_doc.full_name, 'Test Regulatory Document')
        self.assertFalse(self.regulatory_doc.status)

    def test_regulatory_document_update_status(self):
        self.regulatory_doc.update_status()
        self.assertFalse(self.regulatory_doc.status)

        self.task2.status = 'Исполнено'
        self.task2.save()
        self.regulatory_doc.update_status()
        self.assertTrue(self.regulatory_doc.status)
