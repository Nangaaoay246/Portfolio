import streamlit as st
from data import profile, links
import PIL as image
import webbrowser

def configure():
    st.set_page_config(
        page_title='Portfolio - Jan Michael Aoay',
        page_icon='👾',
        layout='wide',
        initial_sidebar_state='expanded'
    ) 

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

def sidebar():
    with st.sidebar:
        st.markdown(f"""
            <div style="text-align: center;">
                <img src="{profile['image_path']}" style="border-radius: 50%; width: 160px; height: 160px; object-fit: cover; margin-bottom: 1rem;">
                <h2>{profile['name']}</h2>
                <p style="color: var(--accent-color)">{profile['title']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📫 Contact ", expanded=True):
            st.html(f"""
                <p>{profile['location']}</p>
                <p>{profile['phone']}</p>
                <p>{profile['email']}</p>
            """)

        social_links()

def social_links():
    link_html = "".join(
        f"""
        <a href="{link['url']}" target="_blank">
            <i class="{link['icon']}"></i>
        </a>
        """
        for link in links)

    st.markdown(
        f"""
        <div style="text-align:center; margin:2rem 2rem;">
            {link_html}
        </div>
        """, unsafe_allow_html=True,
    )

def main():
    configure()
    load_css()
    sidebar()

if __name__ == '__main__':
    main()