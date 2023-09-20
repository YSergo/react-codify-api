from rest_framework import generics
from .models import AboutData
from .serializers import AboutDataSerializer

# Create your views here.
class AboutDataListCreate(generics.ListCreateAPIView):
  queryset = AboutData.objects.all()
  serializer_class = AboutDataSerializer