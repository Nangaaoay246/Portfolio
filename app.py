import streamlit as st
from components.sidebar import sidebar
from components.aboutMe import aboutMe
from components.skillsTab import skillTab
from components.experience import experienceTab

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

# Main ------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    configure()
    load_css()
    sidebar()

    margin_r,body,margin_l = st.columns([0.4, 3, 0.4])
    with body:
        aboutMe()
        skillTab()
        experienceTab()

    