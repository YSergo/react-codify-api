from myapp.models import Projects

data = [
  {
    "title": "Дирекция",
    "description": "Дизайн и разработка страницы объектов для размещения рекламы.",
    "link": "https://codify.software/img/projects/direction.jpg",
    "url_to_project": "https://directionadv.ru/objects/testovyy-obekt"
  },
  {
    "title": "Giftly",
    "description": "UX/UI дизайн и разработка новой социальной сети для авторов контента.",
    "link": "https://codify.software/img/projects/giftly.jpg",
    "url_to_project": None
  },
  {
    "title": "SushiMore",
    "description": "Проектирование дизайна мобильного приложения для сервиса доставки ресторана японской кухни.",
    "link": "https://codify.software/img/projects/sushi.jpg",
    "url_to_project": None
  },
  {
    "title": "Солнце",
    "description": "Разработка в ограниченные сроки сайта для нового детского телеканала «Солнце».",
    "link": "https://codify.software/img/projects/sun.jpg",
    "url_to_project": "https://sun-tv.ru/"
  },
  {
    "title": "Arca Интерьеры",
    "description": "Дизайн и разработка под ключ. ",
    "link": "https://codify.software/img/projects/arca.jpg",
    "url_to_project": "https://arcadesign.ru/"
  }
]

for item in data:
    Projects.objects.create(**item)