from rest_framework import serializers

from accounts.serializers import CustomUserSerializer
from .models import RegulatoryDocument, Task


class TaskSerializer(serializers.ModelSerializer):
    main_executor = CustomUserSerializer(read_only=True)
    co_executors = CustomUserSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'


class RegulatoryDocumentSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = RegulatoryDocument
        fields = '__all__'
