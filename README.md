Порядок запуска приложения:

1. Создать виртуальное окружение:
python -m venv venv

2. Запустить виртуальное окружение:
venv\\Scripts\\activate

3. Установить зависимости:
pip install django djangorestframework psycopg2-binary django-cors-headers

4. Применить миграции:
python manage.py makemigrations

python manage.py migrate

5. Запустить сервер:
python manage.py runserver

Теперь проект доступен по ссылке 127.0.0.1:8000.
