FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code
RUN pip install --upgrade pip && pip install pipenv && pipenv install --system

COPY . /code
