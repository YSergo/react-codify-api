from rest_framework import serializers

from .models import Services, Projects

class ServicesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Services
    fields = ['id', 'title', 'description', 'price']

class ProjectsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ['title', 'description', 'link', 'url_to_project']