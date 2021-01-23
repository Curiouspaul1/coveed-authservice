ARG pyversion=3.8.7-alpine

FROM python:${pyversion}

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt


CMD ["python","wsgi.py"]