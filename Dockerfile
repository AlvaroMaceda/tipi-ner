FROM python:3.6-slim

TO-DO

RUN apt-get update && apt-get install -y git gcc libpcre3-dev poppler-utils tesseract-ocr tesseract-ocr-spa tesseract-ocr-cat antiword

COPY requirements.txt requirements-dev.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app/
WORKDIR /app

ENV FLASK_APP=scanner_backend/app.py

CMD gunicorn --bind 0.0.0.0:5000 --access-logfile - scanner_backend.wsgi:app