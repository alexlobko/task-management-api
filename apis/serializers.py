from rest_framework import serializers

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer
from .models import RegulatoryDocument, Task


class TaskSerializer(serializers.ModelSerializer):
    main_executor_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        source='main_executor',
        write_only=True,
        required=False
    )
    co_executors_ids = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.all(),
        source='co_executors',
        many=True,
        write_only=True,
        required=False,
        allow_null=True,
    )

    regulation_id = serializers.PrimaryKeyRelatedField(
        queryset=RegulatoryDocument.objects.all(),
        source='regulation',
        write_only=True,
        required=False,
        allow_null=True,
        default=None,
    )

    main_executor = CustomUserSerializer(read_only=True)
    co_executors = CustomUserSerializer(many=True, read_only=True)
    regulation = serializers.CharField(source='regulation.__str__', read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class RegulatoryDocumentSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(source='tasks_of_regulation', many=True, read_only=True)

    class Meta:
        model = RegulatoryDocument
        fields = '__all__'

    # def create(self, validated_data):
    #     tasks_data = validated_data.pop('tasks')
    #     document = RegulatoryDocument.objects.create(**validated_data)
    #     document.tasks.set(tasks_data)
    #     return document
    #
    # def update(self, instance, validated_data):
    #     tasks_data = validated_data.pop('tasks')
    #     instance.tasks.set(tasks_data)
    #     return super().update(instance, validated_data)