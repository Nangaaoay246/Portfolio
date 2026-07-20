import streamlit as st
import requests
from constants import *
from components.sidebar import sidebar

# Configure -------------------------------------------------------------------------------------------------------------------------
def configure():
    st.set_page_config(
        page_title='Portfolio - Jan Michael Aoay',
        page_icon='👾',
        layout='wide',
        initial_sidebar_state='expanded'
    ) 

# Load CSS -------------------------------------------------------------------------------------------------------------------------
def load_css():
    st.markdown("""
    <link rel="stylesheet"
          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)

    with open("styles.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

def aboutMe():
    #About me
    st.header("👋 About Me", divider="green")

    col1, col2, col3 = st.columns([1.3 ,0.2, 1])

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

    with col3:
        st.image("assets/nudaeng_laptop.jpg", width=360)

def skillTab():
    st.header("🔨 Technical Skills", divider="green")

    cards = ""
    for category in skills:
        bullets = "".join(
            f"<li>{skill}</li>"
            for skill in category["Skills"]
        )

        cards += f"""
        <div class="skills-card">
            <h3>{category['Type']}</h3>
            <ul>
                {bullets}
            </ul>
        </div>
        """

    st.markdown(
        f"""
        <div class="skills-grid">
            {cards}
        </div>
        """,
        unsafe_allow_html=True,
    )

if __name__ == '__main__':

    configure()
    load_css()
    sidebar()

    margin_r,body,margin_l = st.columns([0.4, 3, 0.4])
    with body:
        aboutMe()
        skillTab()

    