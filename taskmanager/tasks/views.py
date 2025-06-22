from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html' 
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        else:
            return Task.objects.filter(assigned_to=user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'status', 'assigned_to']
    template_name = 'tasks/task_form.html'  
    success_url = reverse_lazy('task-list')

    def test_func(self):
        return self.request.user.is_staff


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'status', 'assigned_to']
    template_name = 'tasks/task_form.html'  
    success_url = reverse_lazy('task-list')

    def test_func(self):
        return self.request.user.is_staff


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def test_func(self):
        return self.request.user.is_staff
