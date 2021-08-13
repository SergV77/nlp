FROM ubuntu:16.04

RUN apt-get update -y \
    apt-get install -y python==3.8 python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY ./

ENTRYPOINT ["python3"]

CMD ["app/app.py"]

