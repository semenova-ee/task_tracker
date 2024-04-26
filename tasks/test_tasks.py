from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Task
from .serializers import TaskSerializer


class TaskViewSetTest(APITestCase):
    def setUp(self):
        # Create some tasks for testing
        self.task1 = Task.objects.create(name="Task 1", deadline="2024-04-30")
        self.task2 = Task.objects.create(name="Task 2", deadline="2024-05-01")

    def test_list_tasks(self):
        url = reverse("task-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data matches the serialized data of all tasks
        expected_data = TaskSerializer(Task.objects.all(), many=True).data
        self.assertEqual(response.data, expected_data)

    def test_create_task(self):
        url = reverse("task-list")
        data = {"name": "New Task", "deadline": "2024-05-15"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().name, "New Task")

    # Add more tests for update and delete operations as needed
