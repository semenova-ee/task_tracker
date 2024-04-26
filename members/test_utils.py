import pytest
from tasks.models import Task
from members.models import Employee
from django.utils import timezone
from django.db.models import Count

from .utils import (
    get_free_tasks,
    get_free_empl,
)


@pytest.fixture
def setup_free_tasks(db):
    # Create tasks with different statuses and employee assignments
    Task.objects.create(
        name="Task 1", status="pending", deadline=timezone.now(), employee=None
    )
    Task.objects.create(
        name="Task 2", status="in_progress", deadline=timezone.now(), employee=None
    )
    Task.objects.create(
        name="Task 3",
        status="pending",
        deadline=timezone.now(),
        employee=Employee.objects.create(username="emp1"),
    )
    Task.objects.create(
        name="Task 4",
        status="pending",
        deadline=timezone.now(),
        employee=Employee.objects.create(username="emp2"),
    )


@pytest.fixture
def setup_free_employees(db):
    # Create employees with different numbers of tasks
    employee1 = Employee.objects.create(username="emp1")
    employee2 = Employee.objects.create(username="emp2")
    Task.objects.create(
        name="Task 5", status="pending", deadline=timezone.now(), employee=employee1
    )
    Task.objects.create(
        name="Task 6", status="pending", deadline=timezone.now(), employee=employee1
    )
    Task.objects.create(
        name="Task 7", status="pending", deadline=timezone.now(), employee=employee2
    )


@pytest.mark.django_db
def test_get_free_tasks(setup_free_tasks):
    # Call the utility function
    free_tasks = get_free_tasks()

    # Assert that the returned tasks are free (have no employee assigned)
    assert all(task.employee is None for task in free_tasks)


@pytest.mark.django_db
def test_get_free_empl(setup_free_employees):
    # Call the utility function
    least_busy_employees, parent_employees = get_free_empl()

    # Assert that the least busy employees have the minimum number of tasks
    min_task_count = min(
        least_busy_employees.annotate(task_count=Count("tasks")).values_list(
            "task_count", flat=True
        )
    )
    assert all(emp.tasks.count() == min_task_count for emp in least_busy_employees)
