from rest_framework import serializers

from .models import Service, Project

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = ['id', 'title', 'description', 'price']

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['id', 'title', 'description', 'link', 'url_to_project']