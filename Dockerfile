FROM amancevice/pandas:1.2.4

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

RUN pwd
CMD [ "python3", "run.py" ]
