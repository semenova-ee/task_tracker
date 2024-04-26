from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee


class UserListCreateAPIViewTest(APITestCase):
    url = reverse("user-list-create")

    def test_list_employees(self):
        Employee.objects.create(username="user1", role="staff")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class UserRetrieveUpdateDestroyAPIViewTest(APITestCase):
    def setUp(self):
        self.employee = Employee.objects.create(username="user1", role="staff")
        self.url = reverse(
            "user-retrieve-update-destroy", kwargs={"pk": self.employee.pk}
        )

    def test_retrieve_employee(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data["username"], "user1"
        )  # Assuming this is the expected username

    def test_delete_employee(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)
