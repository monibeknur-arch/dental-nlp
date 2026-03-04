import streamlit as st
import spacy
from spacy import displacy

# Интерфейс құру
st.title("Стоматологиялық NLP Анализатор")
text = st.text_area("Мәтінді осы жерге жазыңыз:", "Patient has deep caries on tooth 3.6. Treatment: filling.")

# Модельді жүктеу
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# Нәтижені көрсету
if st.button("Талдау"):
    html = displacy.render(doc, style="ent")
    st.write(html, unsafe_allow_html=True)