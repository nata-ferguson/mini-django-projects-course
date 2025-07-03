from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Timesheet(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    week_start = models.DateField()

    monday_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tuesday_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    wednesday_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    thursday_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    friday_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user.username} – {self.task.title} ({self.week_start})"

  