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