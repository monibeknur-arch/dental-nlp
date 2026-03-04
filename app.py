import streamlit as st
import spacy
import os
import subprocess
import sys

# Модельді автоматты түрде жүктеу функциясы
@st.cache_resource
def load_model():
    model_name = "en_core_web_sm"
    try:
        return spacy.load(model_name)
    except OSError:
        # Егер модель табылмаса, оны жүктейміз
        subprocess.check_call([sys.executable, "-m", "spacy", "download", model_name])
        return spacy.load(model_name)

# Модельді іске қосу
nlp = load_model()

# Сайттың интерфейсі
st.title("🦷 Стоматологиялық NLP Анализатор")
st.write("Медициналық есептерді талдауға арналған ИИ жүйесі")

# Мәтін енгізу өрісі
user_input = st.text_area("Мәтінді осы жерге жазыңыз (ағылшынша):", 
                         "Patient A.K. has deep caries on tooth 3.6. Treatment: filling.")

if st.button("Талдау"):
    doc = nlp(user_input)
    
    # Нәтижені түрлі-түсті белгілермен көрсету
    from spacy import displacy
    html = displacy.render(doc, style="ent")
    st.write(html, unsafe_allow_html=True)
