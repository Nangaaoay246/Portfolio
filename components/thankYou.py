import streamlit as st


st.set_page_config(
    page_title="Thank You",
    page_icon="🎉",
    layout="centered"
)
st.markdown("<br><br>", unsafe_allow_html=True)

st.success("Your message has been sent successfully!")

st.markdown(
    """
    # 🎉 Thank You!
    I appreciate you taking the time to reach out.
    I'll review your message and get back to you as soon as I can—usually within **1–3 business days**.
    In the meantime, feel free to explore more of my work or connect with me on LinkedIn or GitHub.
    """
)

col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "🏠 Back to Portfolio",
        "https://your-portfolio.streamlit.app",
        use_container_width=True
    )

with col2:
    st.link_button(
        "💼 View LinkedIn",
        "https://www.linkedin.com/in/jan-michael-aoay/",
        use_container_width=True
    )

st.divider()

st.caption("Thanks again—I look forward to connecting with you!")