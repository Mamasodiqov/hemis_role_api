"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Hemis role API",
        default_version='v1',
        description="API for Hemis role",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="islomiddinmamasodiqov@gmail.com"),
        license=openapi.License(name="demo License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('hemis_api_role/admin/', admin.site.urls),
    path('hemis_api_role/api/v1/', include('role.urls')),

    # swagger
    path('hemis_api_role/swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('hemis_api_role/redoc/', schema_view.with_ui(
             'redoc', cache_timeout=0), name='schema-redoc')
]
