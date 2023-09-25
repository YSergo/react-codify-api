from django.db import models
#  "id": 1,
# "title": "Разработка",
# "description": "Напишем код для сайта или веб-приложения.",
# "price": 60000,
# Create your models here.
class Services(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  price = models.IntegerField()

class Projects(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  link = models.URLField(max_length=200, blank=True, null=True)
  url_to_project = models.URLField(max_length=200, blank=True, null=True)

class Application(models.Model):
  name = models.CharField(max_length=255)
  phone = models.CharField(max_length=20)
  email = models.EmailField()
  request = models.TextField()
