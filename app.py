import streamlit as st
from constants import profile
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
    st.header("About Me", divider="green")
    st.write(profile['info'])

if __name__ == '__main__':
    configure()
    load_css()
    sidebar()
    st.write(profile.keys())

    