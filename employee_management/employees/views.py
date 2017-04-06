from django.views import View
from .models import Employee, Task
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from datetime import datetime
from django.contrib.auth.models import User
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


class AddEmployeeView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['employees.add_employee']
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
        current_date = datetime.now().date()
        ctx = {'tasks': tasks, 'current_date':current_date}
        return render(request, 'employees/active_tasks.html', ctx)


class ToCloseTasksView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(is_active = False, is_closed = False)
        ctx = {'tasks':tasks}
        return render(request, 'employees/to_close.html', ctx)


class TakenTasksView(LoginRequiredMixin, View):
    def get(self, request):
        tasks = Task.objects.filter(is_taken = True)
        ctx = {'tasks':tasks}
        return render(request, 'employees/taken_tasks.html', ctx)


class TaskView(LoginRequiredMixin, View):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        employees = task.employees.all()
        ctx = {'task':task, 'employees':employees}
        return render(request, 'employees/task.html', ctx)


class AddTaskView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ['employees.add_task']
    model = Task
    fields = ['title', 'stand', 'start_date', 'end_date', 'target']
    success_url = '/activetasks/'

    def form_valid(self, form):
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]
        stand = form.cleaned_data["stand"]
        tasks = Task.objects.all()

        if end_date < datetime.now().date():
            form.cleaned_data['is_active'] = False

        if start_date > end_date:
            ctx = {'form': form,
                   'error': "Data rozpoczęcia jest późniejsza niż data zakończenia"}

        for task in tasks:
            if (task.start_date <= start_date <= task.end_date or task.start_date <= end_date <= task.end_date) and task.stand == stand:
                ctx = {'form':form,
                    'error':"Stanowisko jest zajęte w podanym czasie, wybierz inny okres lub inne stanowisko"}
                return render(self.request, 'employees/task_form.html', ctx)

        form.save()
        return HttpResponseRedirect("/alltasks/")


class EditTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['accomplishment', 'is_closed']
    template_name_suffix = '_update_form'
    success_url = '/alltasks/'


class TakeTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['employees', 'is_taken']
    template_name_suffix = '_take_form'
    success_url = '/activetasks/'



