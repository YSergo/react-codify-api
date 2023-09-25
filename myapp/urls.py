from django.urls import path

from . import views
from .views import send_application

urlpatterns = [
    path('services/', views.ServiceListCreate.as_view(), name='get_services'),
    path('projects/', views.ProjectListCreate.as_view(), name='get_projects'),
    path('application/', send_application, name='post_application')
]
