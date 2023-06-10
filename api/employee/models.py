from django.db import models

from api.common.models import Metadata


class Designation(Metadata):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Team(Metadata):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Employee(Metadata):
    name = models.CharField(max_length=255)
    designation = models.ForeignKey(
        "employee.Designation",
        related_name="designation_employee",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        "employee.Team",
        related_name="team_employee",
        on_delete=models.CASCADE,
    )
    manager = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
