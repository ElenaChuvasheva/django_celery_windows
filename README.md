Запуск:
1. сервак локально: python manage.py runserver, открываем главную в браузере
2. контейнер в rabbitmq: docker compose up
3. celery -A DjangoCeleryExample worker -l info -Q queue1 -E --pool=solo, тык на первую кнопку, см. вывод celery

Python 3.5 и выше
