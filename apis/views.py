from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from .models import RegulatoryDocument, Task
from .permissions import IsTaskExecutorOrCoExecutorOrAdmin, IsAdminOrReadOnly
from .serializers import RegulatoryDocumentSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsTaskExecutorOrCoExecutorOrAdmin, IsAdminOrReadOnly]


    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(main_executor=user) | Task.objects.filter(co_executors=user)


class RegulatoryDocumentViewSet(viewsets.ModelViewSet):
    queryset = RegulatoryDocument.objects.all()
    serializer_class = RegulatoryDocumentSerializer
    permission_classes = [IsAdminOrReadOnly]

