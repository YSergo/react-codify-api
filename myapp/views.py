import json
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import ServicesSerializer, ProjectsSerializer
from .models import Services, Projects, Application

# Create your views here.
class ServicesListCreate(generics.ListCreateAPIView):
  queryset = Services.objects.all()
  serializer_class = ServicesSerializer

class ProjectsListCreate(generics.ListCreateAPIView):
  queryset = Projects.objects.all()
  serializer_class = ProjectsSerializer

@csrf_exempt
def send_application(request):
  if request.method == 'POST':
    
    # Парсинг JSON тела запроса
    data = json.loads(request.body.decode('utf-8'))

    # Получение данных формы из тела запроса
    name = data.get('name')
    phone = data.get('phone')
    email = data.get('email')
    request_text = data.get('request')

    # Проверка, что все необходимые поля присутствуют
    if not all([name, phone, email, request_text]):
      return JsonResponse({'error': 'All fields are required'}, status=400)
    
    # Создание и сохранение экземпляра модели
    application = Application(name=name, phone=phone, email=email, request=request_text)
    application.save()
    
    # Возвращение успешного ответа
    return JsonResponse({'status': 'success'}, status=200)
    
    # Если метод запроса не POST, возвращение ошибки
  return JsonResponse({'error': 'Invalid Method'}, status=405)