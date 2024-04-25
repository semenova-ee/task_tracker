from rest_framework.generics import ListAPIView
from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer

class ImportantTasksListView(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Retrieve tasks with pending status
        return Task.objects.filter(status='pending')


class TaskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer