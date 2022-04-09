FROM python:3.7-alpine

RUN apk add gcc g++ musl-dev libffi-dev unixodbc unixodbc-dev psqlodbc

ADD ./src /code

RUN cat /code/_____.ini > /etc/odbcinst.ini

WORKDIR /code

RUN pip install -r _____.txt

EXPOSE 3000

CMD ["_____", "api.py"]
