from django.urls import path, include
from rest_framework.routers import SimpleRouter

from accounts.views import CustomUserViewSet, CurrentUserDetailView
from .views import TaskViewSet, RegulatoryDocumentViewSet

router = SimpleRouter()
router.register('users', CustomUserViewSet, basename='users')
router.register('tasks', TaskViewSet, basename='tasks')
router.register('regulatory-documents', RegulatoryDocumentViewSet, basename='regulatory-documents')


urlpatterns = router.urls + [
    path('current-user', CurrentUserDetailView.as_view(), name='current-user'),
]
