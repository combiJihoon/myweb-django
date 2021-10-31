FROM python:3.8
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD . /home
ADD requirements.txt /home

WORKDIR /home
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
