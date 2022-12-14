FROM python:3.6-slim

RUN pip install gunicorn

RUN apt-get update
RUN apt-get install -y --no-install-recommends git default-libmysqlclient-dev gcc
RUN apt-get purge -y --auto-remove

ENV PYTHONUNBUFFERED 1

ARG ENV_DEBUG=1
ENV DEBUG ENV_DEBUG

ARG ENV_DB_PASS=""
ENV DB_PASS ENV_DB_PASS

ARG ENV_DB_ADDR=""
ENV DB_ADDR ENV_DB_ADDR

ARG ENV_SECRET_KEY="This1s4$tr0ngD38ugK3y"
ENV SECRET_KEY ENV_SECRET_KEY

ENV APP_DIR=/app

RUN mkdir $APP_DIR

COPY LICENSE $APP_DIR
COPY templates $APP_DIR
COPY manage.py $APP_DIR

COPY domain/ $APP_DIR/domain/
COPY personal_site/ $APP_DIR/personal_site/

# TODO: Remove this at some point
COPY *.sqlite3 $APP_DIR

COPY requirements.txt $APP_DIR
# Check the requirements file first to avoid redownloading everything
RUN python -m pip install -r $APP_DIR/requirements.txt

EXPOSE 8000
WORKDIR $APP_DIR
RUN python manage.py collectstatic --noinput
RUN python manage.py makemigrations --noinput
RUN python manage.py migrate --noinput
