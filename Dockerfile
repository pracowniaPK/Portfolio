FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN python -m pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /code/

RUN python /code/manage.py collectstatic --noinput

CMD gunicorn --bind 0.0.0.0:$PORT portfolio.wsgi
