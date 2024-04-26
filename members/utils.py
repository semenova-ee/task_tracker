from django.db.models import Count, Min
from django.db.models import Q
from tasks.models import Task
from members.models import Employee


def get_free_tasks():
    # Filter tasks with a pending status or check if they have child tasks and employee is null
    return Task.objects.filter(
        (Q(status="pending") | Q(child_tasks__isnull=False)) & Q(employee__isnull=True)
    )


def get_free_empl():
    # Step 1: Get the minimum number of tasks among all employees
    min_task_count = Employee.objects.annotate(task_count=Count("tasks")).aggregate(
        min_task_count=Min("task_count")
    )["min_task_count"]

    # Step 2: Get the employees with the minimum number of tasks
    least_busy_employees = Employee.objects.annotate(task_count=Count("tasks")).filter(
        task_count=min_task_count
    )

    # Step 3: Get the employees implementing parent tasks of the free tasks
    parent_tasks = get_free_tasks()
    parent_employees = Employee.objects.filter(tasks__in=parent_tasks).distinct()

    return least_busy_employees, parent_employees


def get_important_tasks_with_possible_employees():
    # Get important tasks
    important_tasks = get_free_tasks()

    # Get possible employees for the tasks
    least_busy_employees, parent_employees = get_free_empl()

    return important_tasks, least_busy_employees, parent_employees
