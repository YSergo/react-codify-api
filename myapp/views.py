from rest_framework import generics
from .models import Services, Projects
from .serializers import ServicesSerializer, ProjectsSerializer

# Create your views here.
class ServicesListCreate(generics.ListCreateAPIView):
  queryset = Services.objects.all()
  serializer_class = ServicesSerializer

class ProjectsListCreate(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer