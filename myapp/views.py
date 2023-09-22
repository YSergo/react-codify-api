from rest_framework import generics
from .models import Services
from .serializers import ServicesSerializer

# Create your views here.
class ServicesListCreate(generics.ListCreateAPIView):
  queryset = Services.objects.all()
  serializer_class = ServicesSerializer