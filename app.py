import streamlit as st
import PIL as image
import webbrowser

PROFILE = "assets\profile.png"
NAME = "Jan Michael Aoay"
TITLE = "👨‍💻 Python Developer & ML Engineer"
LOCATION = "🌏 Cavite, Philippines"
EMAIL = "✉️ aoay.janmichael@gmail.com"
PHONE = "📞 0976 339 2122"

def configure():
    st.set_page_config(
        page_title='Portfolio - Jan Michael Aoay',
        page_icon='👾',
        layout='wide',
        initial_sidebar_state='expanded'
    ) 

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def sidebar():
    with st.sidebar:
        st.image(PROFILE, width=160)
        st.html(f"""
            <div style="text-align: center;">
                <h2>{NAME}</h2>
                <p style="color: var(--accent-color)">{TITLE}</p>
            </div>
        """)
        with st.expander("📫 Contact ", expanded=True):
            st.html(f"""
                <p>{LOCATION}</p>
                <p>{PHONE}</p>
                <p>{EMAIL}</p>
            """)



def main():
    configure()
    load_css()
    sidebar()

if __name__ == '__main__':
    main()