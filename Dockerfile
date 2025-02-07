FROM python:3.9.8-slim

WORKDIR /app
COPY . /app

RUN pip3 install poetry
RUN poetry install

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]