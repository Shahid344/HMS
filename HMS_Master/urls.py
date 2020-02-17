from django.urls import path
from HMS_Master import views


app_name = 'hms_master'

urlpatterns = [

    path('', views.root, name='hms_master_root'),

    path('employee/add/', views.EmployeeCreate.as_view(), name='employee-add'),
    path('employeedetail/', views.EmployeeListView.as_view(), name='employee-detail'),
    path('employee/<int:pk>/', views.EmployeeUpdate.as_view(), name='employee-update'),
    path('employee/<int:pk>/delete/', views.EmployeeDelete.as_view(), name='employee-delete'),
    ]
