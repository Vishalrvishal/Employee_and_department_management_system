from django.shortcuts import render
from .models import Department

# Create your views here.
def home(request):
    return render(request,'home.html')
def department_list(request):
    departments=Department.objects.all()
    return render(request,'department/department_list.html',context={'departments':departments})
def add_department(request):
    if request.method == 'POST':
        department_name = request.POST['dept_name']
        department_head = request.POST['dept_head']
        department_projects = request.POST['dept_projects']
        department_region = request.POST['dept_region']
        department_data=Department(department_name=department_name,department_head=department_head,department_projects=department_projects,department_region=department_region)
        department_data.save()
        return render (request,'deptmessage.html',context={'msg':'Department Added Successfully !!!'})
    return render(request,'department/add_department.html')
def edit_department(request,dept_id):
    department=Department.objects.get(id=dept_id)
    if request.method =='POST':
        department.department_name = request.POST['department_name']
        department.department_head = request.POST['department_head']
        department.department_projects = request.POST['department_projects']
        department.department_region = request.POST['department_region']
        department.save()
        return render(request,'deptmessage.html',context={'msg':'Department Updated Successfully !!!'})
    return render(request,'department/edit_department.html',context={'department':department})
def delete_department(request,dept_id):
    department=Department.objects.get(id=dept_id)
    department.delete()
    return render(request,'deptmessage.html',context={'msg':'Department Deleted Successfully !!!'})
def department_detail(request,dept_id):
    department=Department.objects.get(id=dept_id)
    return render(request,'department/department_detail.html',context={'department':department})
