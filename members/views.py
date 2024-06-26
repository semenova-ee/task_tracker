from rest_framework import generics
from rest_framework.generics import ListAPIView
from django.db import models
from .serializers import EmployeeSerializer, ImportantTaskSerializer
from .models import Employee
from rest_framework.views import APIView
from .utils import get_important_tasks_with_possible_employees
from rest_framework.response import Response

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



class ImportantTasksWithPossibleEmployeesView(APIView):
    def get(self, request):
        # Fetch important tasks and possible employees
        important_tasks, _, _ = get_important_tasks_with_possible_employees()

        # Serialize tasks and employees
        task_serializer = ImportantTaskSerializer(important_tasks, many=True)

        return Response(task_serializer.data)
