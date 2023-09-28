from myapp.models import Project

data = [
  {
    "title": "Дирекция",
    "description": "Дизайн и разработка страницы объектов для размещения рекламы.",
    "image_url": "img/direction.jpg",
    "url_to_project": "https://directionadv.ru/objects/testovyy-obekt"
  },
  {
    "title": "Giftly",
    "description": "UX/UI дизайн и разработка новой социальной сети для авторов контента.",
    "image_url": "img/giftly.jpg",
    "url_to_project": None
  },
  {
    "title": "SushiMore",
    "description": "Проектирование дизайна мобильного приложения для сервиса доставки ресторана японской кухни.",
    "image_url": "img/sushi.jpg",
    "url_to_project": None
  },
  {
    "title": "Солнце",
    "description": "Разработка в ограниченные сроки сайта для нового детского телеканала «Солнце».",
    "image_url": "img/sun.jpg",
    "url_to_project": "https://sun-tv.ru/"
  },
  {
    "title": "Arca Интерьеры",
    "description": "Дизайн и разработка под ключ. ",
    "image_url": "img/arca.jpg",
    "url_to_project": "https://arcadesign.ru/"
  }
]

for item in data:
    Project.objects.create(**item)