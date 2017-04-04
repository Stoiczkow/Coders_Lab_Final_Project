from django.shortcuts import render
from django.views import View
from .models import Employee, Task
from django.shortcuts import render
from django.views.generic.edit import CreateView
# Create your views here.

class MainPageView(View):
    def get(self, request):
        ctx = {}
        return render(request, 'employees/index.html', ctx)


class EmployeesView(View):
    def get(self, request):
        employees = Employee.objects.all().order_by('last_name')
        ctx = {'employees':employees}
        return render(request, 'employees/employees.html', ctx)


class EmployeeView(View):
    def get(self, request, id):
        employee = Employee.objects.get(pk=id)
        tasks = Task.objects.filter(employees=employee)
        ctx = {'employee': employee, 'tasks':tasks}
        return render(request, 'employees/employee.html', ctx)


class AddTaskView(CreateView):
    model = Task
    fields = '__all__'


class AllTasksView(View):
    def get(self, request):
        tasks = Task.objects.all()
        ctx = {'tasks': tasks}
        return render(request, 'employees/tasks.html', ctx)


class TaskView(View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        employees = task.employees.all()
        ctx = {'task':task, 'employees':employees}
        return render(request, 'employees/task.html', ctx)
