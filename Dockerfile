FROM python:3.8
ADD requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]