from rest_framework import status
from rest_framework.views import APIView

from api.common.responses import Response
from api.employee.models import Employee
from api.employee.schemas import EmployeeListSchema
from api.employee.serializers import EmployeeListSerializer


class EmployeeList(APIView):
    permission_classes = []

    @staticmethod
    def get(request):
        employee_data_queryset = Employee.objects.select_related(
            "designation", "team"
        ).all()

        return Response.generate(
            status.HTTP_200_OK,
            "Successfully fetched employee details",
            {"data": EmployeeListSerializer(employee_data_queryset, many=True).data},
        )


class EmployeeDetail(APIView):
    permission_classes = []

    @staticmethod
    def put(request, employee_id):
        try:
            data = EmployeeListSchema.Put(**request.data)
        except Exception as e:
            return Response.request_data_validation_failed(e)

        employee_instance = Employee.objects.filter(id=employee_id).first()
        employee_instance.manager_id = data.manager_id
        employee_instance.save()

        return Response.generate(
            status.HTTP_200_OK,
            "Successfully saved employee details",
        )
