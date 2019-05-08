from django.urls import path

from .views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView
)

urlpatterns = [
    path('', EmployeeListView.as_view()),
    path('create', EmployeeCreateView.as_view()),
    path('<pk>', EmployeeDetailView.as_view()),
    path('<pk>/update/', EmployeeUpdateView.as_view()),
    path('<pk>/delete/', EmployeeDeleteView.as_view())
]