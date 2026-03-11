import streamlit as st
import spacy
from spacy import displacy

# 1. Обязательно раскомментируем кэширование, чтобы модель не грузилась каждый раз
@st.cache_resource
def load_model():
    # 2. Убеждаемся, что имя модели совпадает с установленной в requirements.txt
    return spacy.load("en_core_web_sm")

nlp = load_model()

# Интерфейс
st.title("🦷 Стоматологиялық NLP Анализатор")
st.write("Медициналық есептердегі нысандарды тану")

user_input = st.text_area("Мәтінді енгізіңіз (ағылшынша):", 
                         "Patient A.K. has deep caries on tooth 3.6. Treatment: filling.")

if st.button("Талдау"):
    if user_input:
        doc = nlp(user_input)
        # 3. Визуализация сущностей (Entity Recognition)
        html = displacy.render(doc, style="ent")
        # Чтобы HTML отобразился в Streamlit, используем st.write с параметром unsafe_allow_html
        st.write(html, unsafe_allow_html=True)
    else:
        st.warning("Мәтін енгізіңіз!")


