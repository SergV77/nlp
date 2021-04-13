FROM python:3.7
EXPOSE 5000
COPY requirements.txt /app/requirements.txt

#ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

WORKDIR /app

RUN export PYTHONPATH=/usr/bin/python
RUN pip install -r requirements.txt

COPY . /app
RUN ls -l
RUN pwd
CMD [ "python3", "main.py" ]
