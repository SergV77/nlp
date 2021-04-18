#FROM python:3.7
#EXPOSE 5000
#COPY requirements.txt /app/requirements.txt

#ADD odbcinst.ini /etc/odbcinst.ini
#RUN apt-get update
#RUN apt-get install -y tdsodbc unixodbc-dev
#RUN apt install unixodbc-bin -y
#RUN apt-get clean -y

#FROM gw000/keras-full:latest

#USER root

##ADD odbcinst.ini /etc/odbcinst.ini
#RUN apt-get update -y
#RUN apt-get upgrade -y
##RUN apt-get install -y tdsodbc unixodbc-dev
##RUN apt install unixodbc-bin -y
##RUN apt-get clean -y

#COPY requirements.txt /app/requirements.txt

#WORKDIR /app

#RUN export PYTHONPATH=/usr/bin/python
#RUN pip install -r requirements.txt

#COPY . /app
#RUN ls -l
#RUN pwd
#RUN python3 --version
#CMD [ "python3", "main.py" ]





FROM python:3.5

MAINTAINER Julien Maupetit <julien@tailordev.fr>

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran

RUN mkdir -p /opt/pandas/build/

COPY requirements.txt /opt/pandas/build/requirements.txt

RUN pip install -r /opt/pandas/build/requirements.txt
