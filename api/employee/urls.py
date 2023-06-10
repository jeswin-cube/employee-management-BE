from django.urls import path

from api.employee.views import EmployeeList, EmployeeDetail

app_name = "api.employee"

urlpatterns = [
    path(
        "<int:employee_id>",
        EmployeeDetail.as_view(),
        name="employee_list",
    ),
    path(
        "",
        EmployeeList.as_view(),
        name="employee_list",
    ),
]
