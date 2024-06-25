# Generated by Django 5.0.6 on 2024-06-25 12:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('deadline', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[(True, 'Исполнено'), (False, 'Не исполнено')], default='Не исполнено', max_length=100)),
                ('co_executors', models.ManyToManyField(blank=True, related_name='co_tasks', to=settings.AUTH_USER_MODEL)),
                ('main_executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegulatoryDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_type', models.CharField(blank=True, choices=[('Протокол', 'Протокол'), ('Решение', 'Решение'), ('Приказ', 'Приказ'), ('Распоряжение', 'Распоряжение')], max_length=100, null=True)),
                ('date_approved', models.DateField()),
                ('registration_number', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=255)),
                ('tasks', models.ManyToManyField(related_name='regulatory_documents', to='apis.task')),
            ],
        ),
    ]
