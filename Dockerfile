FROM python:3.8-slim AS base

COPY . /app/
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .

FROM base as recursive-dict-tests
