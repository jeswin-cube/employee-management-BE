from rest_framework import status
from rest_framework.views import APIView

from api.common.responses import Response


class HealthCheckDetail(APIView):
    permission_classes = []
    authentication_classes = []

    @staticmethod
    def get(request):
        return Response.generate(status.HTTP_200_OK, "Health Check Successful")
