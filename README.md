# bostongene

Чтобы запустить проект необходимо установить библиотеки из requirements.txt

pip install --user --requirement requirements.txt

Установить переменную среды FLASK_APP:

export FLASK_APP=app.py

В файле config.py изменить переменные MAIL_USERNAME, MAIL_PASSWORD, в routes.py заменить sender в 29 строке.

Запустить Redis коммандой redis-server

Выполнить команда celery -A app.celery worker

Запустиь Flask командой flask run.
