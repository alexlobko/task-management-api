from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TaskViewSet, RegulatoryDocumentViewSet

router = SimpleRouter()
router.register('tasks', TaskViewSet, basename='tasks')
router.register('regulatory-documents', RegulatoryDocumentViewSet, basename='regulatory-documents')


urlpatterns = router.urls
