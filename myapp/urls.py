from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.AboutDataListCreate.as_view(), name='item-list-create'),
]
