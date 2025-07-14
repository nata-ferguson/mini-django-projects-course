from django.shortcuts import render
from django.http import HttpResponse 
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import TimesheetForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import Task, Timesheet

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
    

class TimesheetCreateView(LoginRequiredMixin, CreateView):
    model = Timesheet
    form_class = TimesheetForm
    template_name = 'tasks/timesheet_form.html'
    success_url = reverse_lazy('timesheet-list')  

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.status = 'pending'
        return super().form_valid(form)

class TimesheetListView(LoginRequiredMixin, ListView):
    model = Timesheet
    template_name = 'tasks/timesheet_list.html'
    context_object_name = 'timesheets'

    def get_queryset(self):
        return Timesheet.objects.filter(user=self.request.user).order_by('-week_start')
    
class ManagerTimesheetListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Timesheet
    template_name = 'tasks/manager_dashboard.html'
    context_object_name = 'timesheets'

    def test_func(self):
        return self.request.user.is_staff
    
    def get_queryset(self):
        queryset = Timesheet.objects.all()
        status_filter = self.request.GET.get('status')
        user_filter = self.request.GET.get('user')

        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if user_filter:
            queryset = queryset.filter(user__username=user_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Timesheet.STATUS_CHOICES
        context['users'] = User.objects.order_by('username')
        context['selected_status'] = self.request.GET.get('status', '')
        context['selected_user'] = self.request.GET.get('user', '')
        return context


