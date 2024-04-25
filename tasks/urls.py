from rest_framework import routers
from .views import TaskViewSet, ImportantTasksListView
from django.urls import path

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('important-tasks/', ImportantTasksListView.as_view(), name='important_tasks_list'),
]

urlpatterns += router.urls