# bostongene

Чтобы запустить проект необходимо установить библиотеки из requirements.txt

<code>pip install --user --requirement requirements.txt</code>

Установить переменную среды FLASK_APP:

<code>export FLASK_APP=app.py</code>

В файле config.py изменить переменные MAIL_USERNAME, MAIL_PASSWORD, в routes.py заменить sender в 29 строке.

Запустить Redis коммандой 

<code>redis-server</code>

Выполнить команда 

<code>celery -A app.celery worker</code>

Запустиь Flask командой flask run.
