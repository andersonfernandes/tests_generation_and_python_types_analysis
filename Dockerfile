FROM python:3.10.11-slim-buster

RUN apt update && apt install -y git

RUN mkdir /home/app
WORKDIR /home/app

COPY scrapy/tests/requirements.txt ./scrapy_requirements.txt

RUN pip install \
      pynguin \
      w3lib \
      scrapy \
      mutatest \
      sybil \
      testfixtures \
      sphinx_rtd_theme \
      coverage \
      botocore \
      -r scrapy_requirements.txt

RUN rm scrapy_requirements.txt
