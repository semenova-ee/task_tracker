from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Employee
from tasks.serializers import TaskSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = ["role", "username", "password", "tasks", "name"]
        ref_name = 'CustomUserSerializer'

    def create(self, validated_data):
        password = validated_data.get('password')

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password

        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password

        user = super().update(instance, validated_data)
        return user
