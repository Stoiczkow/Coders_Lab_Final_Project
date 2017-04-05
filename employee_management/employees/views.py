from django.shortcuts import render, redirect
from django.views import View
from .models import Employee, Task
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from datetime import datetime
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your views here.

def task_date_check(tasks):
    current_date = datetime.now().date()
    for task in tasks:
        if task.end_date < current_date:
            task.is_active = False
            task.save()
        else:
            task.is_active = True
            task.save()

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {'form':form}
        return render(request, 'employees/login.html', ctx)

    def post(self, request):
        form = LoginForm()
        ctx = {'form': form}
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "employees/login.html", ctx)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class MainPageView(LoginRequiredMixin, View):
    def get(self, request):
        ctx = {}
        return render(request, 'employees/index.html', ctx)


class EmployeesView(LoginRequiredMixin,View):
    def get(self, request):
        employees = Employee.objects.all().order_by('last_name')
        ctx = {'employees':employees}
        return render(request, 'employees/employees.html', ctx)


class EmployeeView(LoginRequiredMixin,View):
    def get(self, request, id):
        employee = Employee.objects.get(pk=id)
        tasks = Task.objects.filter(employees=employee)
        ctx = {'employee': employee, 'tasks':tasks}
        return render(request, 'employees/employee.html', ctx)


class AddEmployeeView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'


class EditEmployeeView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = "__all__"
    template_name_suffix = '_update_form'


class AllTasksView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.all().order_by('-end_date')
        task_date_check(tasks)
        ctx = {'tasks': tasks}
        return render(request, 'employees/tasks.html', ctx)

class ActiveTasksView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(is_active=True).order_by('-end_date')
        task_date_check(tasks)
        ctx = {'tasks': tasks}
        return render(request, 'employees/active_tasks.html', ctx)

class TaskView(LoginRequiredMixin, View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        employees = task.employees.all()
        current_date = datetime.now().date()
        ctx = {'task':task, 'employees':employees, 'current_date':current_date}
        return render(request, 'employees/task.html', ctx)


class AddTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = "__all__"

    def form_valid(self, form):
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]
        stand = form.cleaned_data["stand"]
        tasks = Task.objects.all()

        for task in tasks:
            if (task.start_date <= start_date <= task.end_date or task.start_date <= end_date <= task.end_date) and task.stand == stand:
                return HttpResponse("Źleeee")
                #raise ValidationError("Stanowisko jest zajęte w podanym czasie")

        form.save()
        return HttpResponseRedirect("/alltasks/")