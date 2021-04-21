FROM python:3.8-slim AS base

COPY . /app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

FROM base as recursive-dict-tests
