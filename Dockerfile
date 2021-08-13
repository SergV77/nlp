FROM debian

RUN apt-get update -y && apt-get install python3-pip -y && pip3 install pip --upgrade && apt-get clean

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app/app.py"]

