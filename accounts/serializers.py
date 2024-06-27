from rest_framework import serializers
from accounts.models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['full_name']


class CustomUserListSerializer(serializers.ModelSerializer):
    deputy = CustomUserSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'position', 'deputy']


class CustomUserDetailSerializer(serializers.ModelSerializer):
    from apis.serializers import TaskSerializer

    main_tasks = TaskSerializer(many=True, read_only=True)
    co_tasks = TaskSerializer(many=True, read_only=True)
    deputy = CustomUserSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'full_name', 'position', 'deputy', 'main_tasks', 'co_tasks']
