FROM python:3.10.11-slim-buster
# https://hub.docker.com/_/django
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt
# https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application
COPY . /code/

EXPOSE 80

CMD python manage.py runserver 0.0.0.0:8000

# https://www.youtube.com/watch?v=UV55ehkX16A&t=828s
