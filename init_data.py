from myapp.models import AboutData

data = [
  {
    "title": "Разработка",
    "description": "Напишем код для сайта или веб-приложения.",
    "price": 60000
  },
  {
    "title": "UX/UI дизайн",
    "description": "Решим проблемы бизнеса с помощью UX/UI дизайна.",
    "price": 50000
  },
  {
    "title": "Хочу все",
    "description": "Спроектируем продукт и реализуем его под ключ.",
    "price": 120000
  },
  {
    "title": "Поддержка",
    "description": "Поддерживаем работу сайта или веб-приложения ежедневно.",
    "price": 30000
  },
  {
    "title": "Доработка",
    "description": "Внедрим новую функциональность или доработаем существующую.",
    "price": 5000
  },
  {
    "title": "No-code",
    "description": "В 3 раза быстрее и дешевле без потери мощности.",
    "price": 24000
  }
]

for item in data:
    AboutData.objects.create(**item)