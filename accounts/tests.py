from django.test import TestCase
from django.contrib.auth.models import Permission

from apis.models import Task
from .models import CustomUser


class CustomUserTestCase(TestCase):

    def setUp(self):
        self.user1 = CustomUser.objects.create(
            username='user1',
            full_name='User One',
            position='Employee',
        )

        self.user2 = CustomUser.objects.create(
            username='user2',
            full_name='User Two',
            position='Employee 2',
            deputy=self.user1
        )

        self.user3 = CustomUser.objects.create(
            username='user3',
            full_name='User Three',
            position='Manager',
            deputy=self.user2
        )
        self.task1 = Task.objects.create(
            content='Task One',
            main_executor=self.user2,

        )
        self.task2 = Task.objects.create(
            content='Task Two',
            main_executor=self.user3,
        )
        self.task2.co_executors.set([self.user2])

    def test_full_name_method(self):
        self.assertEqual(self.user1.full_name, 'User One')

    def test_position_method(self):
        self.assertEqual(self.user1.position, 'Employee')

    def test_deputy_method(self):
        self.assertEqual(self.user1.deputy, None)
        self.assertEqual(self.user2.deputy, self.user1)
        self.assertEqual(self.user3.deputy, self.user2)

    def test_main_tasks_method(self):
        self.assertEqual(self.user1.main_tasks.all().count(), 0)
        self.assertEqual(self.user2.main_tasks.all().count(), 1)
        self.assertEqual(self.user3.main_tasks.all().count(), 1)

    def test_co_executors_tasks_method(self):
        self.assertEqual(self.user1.co_executors_tasks.all().count(), 0)
        self.assertEqual(self.user2.co_executors_tasks.all().count(), 1)
        self.assertEqual(self.user3.co_executors_tasks.all().count(), 0)

    def test_str_method(self):
        self.assertEqual(str(self.user1), 'User One')

    def test_delete_method(self):
        self.user2.delete()
        self.assertFalse(CustomUser.objects.filter(pk=self.user2.id).exists())
        self.user3.refresh_from_db()
        self.assertEqual(self.user3.deputy, self.user1)
        self.assertEqual(Task.objects.get(pk=self.task1.id).main_executor, self.user1)
        self.assertNotIn(self.user2, Task.objects.get(pk=self.task2.id).co_executors.all())
        self.assertIn(self.user1, Task.objects.get(pk=self.task2.id).co_executors.all())
