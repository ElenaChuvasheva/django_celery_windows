Запуск:
1. сервак локально: python manage.py runserver, открываем главную в браузере
2. контейнер с rabbitmq: docker compose up
3. celery -A DjangoCeleryExample worker -l info -Q queue1 -E --pool=solo, тык на первую кнопку, см. вывод celery

Если нужна периодическая задача: после запуска сервера и rabbit
1. celery -A DjangoCeleryExample worker -l info --pool=solo
2. celery -A DjangoCeleryExample beat -l info

Python 3.5 и выше, Windows 10