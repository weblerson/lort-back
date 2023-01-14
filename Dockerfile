FROM python:3.10-slim

ENV PYTHONBUFFERED=1
WORKDIR = /APP

RUN apt update

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
