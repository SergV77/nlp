FROM amancevice/pandas:1.2.4

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN pwd
RUN python3 --version
CMD [ "python3", "main.py" ]
