from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServicesListCreate.as_view(), name='get_services'),
    path('projects/', views.ProjectsListCreate.as_view(), name='get_projects'),
]
