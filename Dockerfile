FROM python:3.8

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app app

RUN pwd

EXPOSE 5000
ENTRYPOINT ["python3", "run.py"]
