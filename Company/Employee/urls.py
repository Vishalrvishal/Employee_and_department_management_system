from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name='home'),
    path('employee/add/',employee_add,name='add employee'),
    path('employee/view/',employee_view, name='view employee'),
    path('employee/view/<emp_id>/',employee_view_id, name='view employee id'),
    path('employee/delete/<emp_id>/',employee_delete, name='delete employee'),
    path('employee/edit/<emp_id>/',employee_edit, name='edit employee')
]