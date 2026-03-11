import streamlit as st
import spacy
from spacy import displacy

# Кэшируем модель, чтобы приложение не падало от нехватки памяти
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

st.title("🦷 Стоматологиялық NLP Анализатор")
st.write("Медициналық есептерді талдау")

user_input = st.text_area("Мәтінді енгізіңіз (ағылшынша):", 
                         "Patient has deep caries on tooth 3.6.")

if st.button("Талдау"):
    if user_input:
        doc = nlp(user_input)
        # Генерируем HTML для визуализации сущностей
        html = displacy.render(doc, style="ent")
        # Отображаем результат в Streamlit
        st.write(html, unsafe_allow_html=True)
    else:
        st.warning("Мәтін енгізіңіз!")
