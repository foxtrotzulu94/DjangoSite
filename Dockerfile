FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV DEBUG 1

# Check the requirements file first to avoid redownloading everything
ADD requirements.txt /
RUN python -m pip install -r /requirements.txt

# TODO: Fix the "copy everything you find" step
COPY . /
EXPOSE 8000

RUN python /manage.py collectstatic --noinput
RUN python /manage.py makemigrations --noinput
RUN python /manage.py migrate --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
