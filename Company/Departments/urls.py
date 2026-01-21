from django.urls import path
from .views import*

urlpatterns = [
    path('',home,name='department home'),
    path('department/list/',department_list, name='department list'),
    path('department/add/',add_department, name='add department'),
    path('department/edit/<dept_id>/',edit_department, name='edit department'),
    path('department/delete/<dept_id>/',delete_department, name='delete department'),
    path('department/details/<dept_id>/',department_detail, name='department details'),
]
