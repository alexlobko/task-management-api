from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer, CustomUserListSerializer, CustomUserDetailSerializer


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CustomUserListSerializer
        return CustomUserDetailSerializer

    @action(detail=True, methods=['get'])
    def detail(self, request, pk=None):
        user = self.get_object()
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)


class CurrentUserDetailView(generics.RetrieveAPIView):
    serializer_class = CustomUserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user