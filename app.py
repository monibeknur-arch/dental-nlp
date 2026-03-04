import streamlit as st
import spacy
from spacy import displacy

# Модельді жүктеу (ол requirements арқылы алдын ала орнатылады)
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Интерфейс
st.title("🦷 Стоматологиялық NLP Анализатор")
st.write("Медициналық есептердегі нысандарды тану")

user_input = st.text_area("Мәтінді енгізіңіз (ағылшынша):", 
                         "Patient A.K. has deep caries on tooth 3.6. Treatment: filling.")

if st.button("Талдау"):
    doc = nlp(user_input)
    # Нәтижені визуализациялау
    html = displacy.render(doc, style="ent")
    st.write(html, unsafe_allow_html=True)
