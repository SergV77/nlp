FROM python:3.8

WORKDIR .
COPY . /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["run.py"]
