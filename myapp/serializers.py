from rest_framework import serializers
from .models import AboutData

class AboutDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = AboutData
    fields = ['id', 'title', 'description', 'price']