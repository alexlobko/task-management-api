from rest_framework import serializers
from .models import RegulatoryDocument, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class RegulatoryDocumentSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = RegulatoryDocument
        fields = '__all__'
