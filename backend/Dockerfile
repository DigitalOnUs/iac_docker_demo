FROM python:3.6-alpine

RUN apk update && apk upgrade && \
    apk add make gcc python3-dev musl-dev --no-cache

COPY ./requirements.txt /

RUN pip install -r requirements.txt

RUN mkdir /usr/src/forbackend
COPY ./ /usr/src/forbackend
WORKDIR /usr/src/forbackend

EXPOSE 8000

CMD ["python", "webserver.py"]
