FROM python:3

#COPY requirements.txt /app/requirements.txt

#RUN pip install -r requirements.txt
#RUN python -m spacy download ru_core_news_lg
COPY . /app

WORKDIR /app

RUN pwd
RUN python3 --version
CMD [ "python3", "streamlit_app.py" ]
