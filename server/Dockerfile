FROM python:3.9.4-slim

RUN apt-get update
RUN apt-get install -y git libpq-dev postgresql-client

WORKDIR /server

COPY ./server /server

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]