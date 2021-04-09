FROM python:3.7

COPY requirements.txt /app/requirements.txt

ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

WORKDIR /app

RUN export PYTHONPATH=/usr/bin/python
RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "./main.py" ]
