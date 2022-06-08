FROM python:3.10.4

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD req.txt /code/
RUN pip install -r requirements.txt
ADD ./. /code/

EXPOSE 8000
