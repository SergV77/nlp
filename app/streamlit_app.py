from spacy_streamlit import *
import spacy
from spacy_streamlit import process_text
from spacy_streamlit import visualize_similarity
import streamlit as st
from spacy_streamlit import load_model

models = ["ru_core_news_lg"]
default_text = "Шаблонный текст для примера."

st.title("Синтаксический разбор")

visualize(models, default_text)
