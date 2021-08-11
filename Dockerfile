FROM python:3

WORKDIR /app

#COPY requirements.txt /app/requirements.txt

#RUN pip install -r requirements.txt
#RUN python -m spacy download ru_core_news_lg
COPY . .

RUN ls

RUN pwd
RUN python3 --version
CMD [ "python3", "streamlit_app.py" ]
