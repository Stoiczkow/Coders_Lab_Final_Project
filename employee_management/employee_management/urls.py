"""employee_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from employees.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/', LogoutView.as_view(), name="logout"),
    url(r'^index/$', MainPageView.as_view(), name="index"),
    url(r'^employees/$', EmployeesView.as_view(), name="employees"),
    url(r'^employee/(?P<id>(\d)+)/$', EmployeeView.as_view(), name="employee"),
    url(r'^addemployee/$', AddEmployeeView.as_view(), name="add_employee"),
    url(r'^editemployee/(?P<pk>(\d)+)/$', EditEmployeeView.as_view(), name="edit_employee"),
    url(r'^addtask/$', AddTaskView.as_view(), name="add_task"),
    url(r'^alltasks/$', AllTasksView.as_view(), name="all_tasks"),
    url(r'^taketask/(?P<pk>(\d)+)/$', TakeTaskView.as_view(), name="take_task"),
    url(r'^activetasks/$', ActiveTasksView.as_view(), name="active_tasks"),
    url(r'^takentasks/$', TakenTasksView.as_view(), name="taken_tasks"),
    url(r'^toclosetasks/$', ToCloseTasksView.as_view(), name="to_close_tasks"),
    url(r'^task/(?P<id>(\d)+)/$', TaskView.as_view(), name="task"),
    url(r'^edittask/(?P<pk>(\d)+)/$', EditTaskView.as_view(), name="edit_task"),

]
