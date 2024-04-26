from .models import Task
from rest_framework import viewsets
from .serializers import TaskSerializer



class TaskViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer