FROM python:3.8-slim-buster

ARG ROOT_PATH=/app

WORKDIR ${ROOT_PATH}

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY setup.py .
RUN pip install -e .

COPY . .
