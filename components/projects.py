import streamlit as st
from constants import projects

def projectTab():
    st.header("🚀 Projects", divider="green")

    cards = ""

    for project in projects:
        cards += f"""
        <a href="{project['Link']}" target="_blank" class="project-card">
            <div>
                <img src="{project['Image']}" class="project-image">
                <div class="project-content">
                    <h3>{project['Title']} ↗</h3>
                    <p>{project['Description']}</p>
                    <span class="project-tech">{project['Tech']}</span>
                </div>
            </div>
        </a>
        """
    st.markdown(
        f"""
        <div class="projects-grid">
            {cards}
        </div>
        """,
        unsafe_allow_html=True,
    )

