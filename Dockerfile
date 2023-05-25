FROM python:3.10.11-slim-buster

RUN apt update && apt install -y git

RUN mkdir /home/app
WORKDIR /home/app

COPY requirements.txt ./requirements.txt
COPY scrapy/tests/requirements.txt ./scrapy_requirements.txt

RUN pip install -r requirements.txt \
      -r scrapy_requirements.txt

RUN rm requirements.txt \
       scrapy_requirements.txt
