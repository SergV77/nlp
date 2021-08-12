FROM python:3.8

WORKDIR /app

COPY . .

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "./run.py"]
