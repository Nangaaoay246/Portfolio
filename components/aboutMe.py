import streamlit as st
import requests
from constants import profile

def aboutMe():
    #About me
    st.header("👋 About Me", divider="green")

    col1, col2 = st.columns([1.5, 1] ,vertical_alignment='center')

    with col1:
        st.markdown(profile['info'])

        url = "https://github.com/Nangaaoay246/Portfolio/raw/main/assets/JanMichaelJAoay_Resume.pdf"

        response = requests.get(url)

        if response.status_code == 200:
            pdf_file = response.content

        st.download_button(
            label="Download my :green[resume]",
            data=pdf_file,
            file_name="JanMichaelAoay_resume.pdf",
            mime="application/pdf")

    with col2:
        st.image("assets/nudaeng_laptop.jpg", width=360)