from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework import serializers
from .models import Employee
from tasks.serializers import TaskSerializer
from tasks.models import Task
from .utils import get_free_empl


class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ["role", "username", "password", "tasks", "name"]
        ref_name = "CustomUserSerializer"

    def create(self, validated_data):
        password = validated_data.get("password")

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data["password"] = hashed_password

        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.get("password")

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data["password"] = hashed_password

        user = super().update(instance, validated_data)
        return user


class ImportantTaskSerializer(serializers.ModelSerializer):
    possible_employee = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "parent_task_url",
            "deadline",
            "status",
            "possible_employee",
        ]

    def get_possible_employee(self, obj):
        # Retrieve possible employees for the task
        least_busy_employees, parent_employees = get_free_empl()

        # Generate URLs for each possible employee
        employee_urls = [
            "http://127.0.0.1:8000"
            + reverse("user-retrieve-update-destroy", kwargs={"pk": emp.id})
            for emp in least_busy_employees
        ]

        return employee_urls
