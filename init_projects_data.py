from myapp.models import Project

data = [
  {
    "title": "Дирекция",
    "description": "Дизайн и разработка страницы объектов для размещения рекламы.",
    "link": "https://apialisada11-721689c1d185.herokuapp.com/static/img/direction.jpg",
    "url_to_project": "https://directionadv.ru/objects/testovyy-obekt"
  },
  {
    "title": "Giftly",
    "description": "UX/UI дизайн и разработка новой социальной сети для авторов контента.",
    "link": "https://apialisada11-721689c1d185.herokuapp.com/static/img/giftly.jpg",
    "url_to_project": None
  },
  {
    "title": "SushiMore",
    "description": "Проектирование дизайна мобильного приложения для сервиса доставки ресторана японской кухни.",
    "link": "https://apialisada11-721689c1d185.herokuapp.com/static/img/sushi.jpg",
    "url_to_project": None
  },
  {
    "title": "Солнце",
    "description": "Разработка в ограниченные сроки сайта для нового детского телеканала «Солнце».",
    "link": "https://apialisada11-721689c1d185.herokuapp.com/static/img/sun.jpg",
    "url_to_project": "https://sun-tv.ru/"
  },
  {
    "title": "Arca Интерьеры",
    "description": "Дизайн и разработка под ключ. ",
    "link": "https://apialisada11-721689c1d185.herokuapp.com/static/img/arca.jpg",
    "url_to_project": "https://arcadesign.ru/"
  }
]

for item in data:
    Project.objects.create(**item)