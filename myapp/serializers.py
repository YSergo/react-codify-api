from rest_framework import serializers

from .models import Service, Project

class ServiceSerializer(serializers.ModelSerializer):
  class Meta:
    model = Service
    fields = ['id', 'title', 'description', 'price']

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ['id', 'title', 'description', 'image_url', 'url_to_project']