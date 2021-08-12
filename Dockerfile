FROM python:3.8


COPY .

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["run.py"]
