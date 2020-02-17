from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# from HMS_Master.models import*
from HMS_Master.forms import*


def root(request):
    return render(request, 'page/hms_master_root.html')


# ***************************** Employee Master ************************************


class EmployeeListView(generic.ListView):
    model = Employee
    template_name = 'page/employee/employee_detail.html'
    context_object_name = 'all_employee'

    def get_queryset(self):
        return Employee.objects.all()


class EmployeeCreate(SuccessMessageMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'page/employee/employee_form.html'
    success_url = reverse_lazy('hms_master:employee-add')
    success_message = "%(emp_name)s is created successfully"

    # def form_valid(self, form):
    #     # add a log after save or whatever
    #     super(EmployeeCreate, self).form_valid(self, form)


class EmployeeUpdate(SuccessMessageMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'page/employee/employee_form.html'
    success_url = reverse_lazy('hms_master:employee-add')
    success_message = "%(emp_name)s is updated successfully"


class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'page/employee/delete.html'
    success_url = reverse_lazy('hms_master:employee-detail')
