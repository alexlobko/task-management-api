from rest_framework import viewsets
from .models import RegulatoryDocument, Task
from .serializers import RegulatoryDocumentSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class RegulatoryDocumentViewSet(viewsets.ModelViewSet):
    queryset = RegulatoryDocument.objects.all()
    serializer_class = RegulatoryDocumentSerializer
