from rest_framework import serializers

from api.common.serializers import MetadataSerializer
from api.employee.models import Designation, Employee, Team


class DesignationSerializer(MetadataSerializer, serializers.ModelSerializer):
    class Meta(MetadataSerializer.Meta):
        model = Designation
        fields = "__all__"


class TeamSerializer(MetadataSerializer, serializers.ModelSerializer):
    class Meta(MetadataSerializer.Meta):
        model = Team
        fields = "__all__"


class EmployeeListSerializer(MetadataSerializer, serializers.ModelSerializer):
    team = TeamSerializer()
    designation = DesignationSerializer()

    class Meta(MetadataSerializer.Meta):
        model = Employee
        fields = "__all__"
