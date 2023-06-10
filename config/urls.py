"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .health import HealthCheckDetail

# This handler only works when debug is set to false, so will work in prod
handler500 = "api.common.exceptions.server_error"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health", HealthCheckDetail.as_view(), name="health_check_details"),
    path("employee/", include("api.employee.urls", "employee"))
]
