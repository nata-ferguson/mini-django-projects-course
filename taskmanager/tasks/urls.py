from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TimesheetCreateView,
    TimesheetListView
)



urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('timesheets/submit/', TimesheetCreateView.as_view(), name='timesheet-submit'),
    path('timesheets/', TimesheetListView.as_view(), name='timesheet-list'),

]


