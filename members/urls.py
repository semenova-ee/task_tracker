from django.urls import path
from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserTaskCountListView,
    ImportantTasksWithPossibleEmployeesView,
)

urlpatterns = [
    path("", UserListCreateAPIView.as_view(), name="user-list-create"),
    path(
        "<int:pk>/",
        UserRetrieveUpdateDestroyAPIView.as_view(),
        name="user-retrieve-update-destroy",
    ),
    path("busy-users/", UserTaskCountListView.as_view(), name="busy-users"),
    path(
        "important-tasks/",
        ImportantTasksWithPossibleEmployeesView.as_view(),
        name="important_tasks_list",
    ),
]
