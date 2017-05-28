FROM python:2.7-slim

RUN pip install nose

WORKDIR /src

COPY . ./
CMD nosetests
