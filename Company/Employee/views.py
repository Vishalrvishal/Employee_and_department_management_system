from django.shortcuts import render
from .models import Employee
# Create your views here.
def home(request):
    return render(request,'home.html')
def employee_add(request):
    if request.method == 'POST':
        employee_name=request.POST['emp_name']
        employee_age=request.POST['emp_age']
        employee_address=request.POST['emp_address']
        employee_department=request.POST['emp_department']
        employee_reporting_manager=request.POST['emp_reporting_manager']
        employee_email=request.POST['emp_email']
        employee_data=Employee(employee_name=employee_name,employee_age=employee_age,employee_address=employee_address,employee_department=employee_department,employee_reporting_manager=employee_reporting_manager,employee_email=employee_email)
        employee_data.save()
        return render (request,'empmessage.html',context={'msg':'Employee data added successfully !!!'})
    return render(request,'employee/add.html')
def employee_view(request):
    employees=Employee.objects.all()
    return render(request,'employee/view.html',context={'employees':employees})
def employee_view_id(request,emp_id):
    employee=Employee.objects.get(id=emp_id)
    return render(request,'employee/view_id.html',context={
        'employee': employee
    })
def employee_delete(request,emp_id):
    employee=Employee.objects.get(id=emp_id)
    employee.delete()
    return render (request,'empmessage.html',context={'msg':'Employee data deleted successfully !!!'})

def employee_edit(request,emp_id):
    employee=Employee.objects.get(id=emp_id)
    if request.method=='POST':
        employee.employee_name=request.POST["emp_name"]
        employee.employee_age=request.POST['emp_age']
        employee.employee_address=request.POST['emp_address']
        employee.employee_department=request.POST['emp_department']
        employee.employee_reporting_manager=request.POST['emp_reporting_manager']
        employee.employee_email=request.POST['emp_email']
        employee.save()
        return render (request,'empmessage.html',context={'msg':'Employee data updated successfully!!!'})
    return render(request,'employee/edit.html',context={
        'employee':employee
    })
