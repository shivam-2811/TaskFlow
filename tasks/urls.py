from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("<int:task_id>/toggle/", views.toggle_task, name="toggle_task"),
    path("<int:task_id>/delete/", views.delete_task, name="delete_task"),
]
taskflow/urls.py:

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("tasks.urls")),
    path("clear-completed/", views.clear_completed, name="clear_completed"),
]

