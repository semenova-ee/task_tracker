from django.db import models
from django.urls import reverse
from members.models import Employee

class Task(models.Model):
    name = models.CharField(max_length=100)
    parent_task_url = models.URLField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True)
    deadline = models.DateTimeField()
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    child_tasks = models.ManyToManyField('self', symmetrical=False, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])
