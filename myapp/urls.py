from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.ServicesListCreate.as_view(), name='item-list-create'),
]
