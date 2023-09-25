from django.urls import path

from . import views
from .views import send_application

urlpatterns = [
    path('services/', views.ServicesListCreate.as_view(), name='get_services'),
    path('projects/', views.ProjectsListCreate.as_view(), name='get_projects'),
    path('application/', send_application, name='post_application')
]
