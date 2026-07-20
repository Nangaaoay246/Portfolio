import streamlit as st
from constants import skills

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