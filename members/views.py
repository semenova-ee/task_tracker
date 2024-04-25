from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.db import models
from .serializers import EmployeeSerializer
from .models import Employee


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UserTaskCountListView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # Retrieve all employees sorted by the number of tasks they have
        return Employee.objects.annotate(task_count=models.Count('tasks')).order_by('-task_count')
