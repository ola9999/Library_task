from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi 
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title= "Api Docs",
        default_version="v1",
        description="init api docs",
        terms_of_service=" ",
        contact=openapi.Contact(email = " "),
        license=openapi.License(name = " ")),

    public= True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',  include('apps.api.urls')),
    path(
        'swagger',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),

]
