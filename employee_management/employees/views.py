from django.shortcuts import render
from django.views import View
from .models import Employee
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

class AssignTaskView(View):
    