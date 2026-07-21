import streamlit as st

def contactTab():
    contactForm = """ 
    <form action="https://formsubmit.co/aoay.janmichael@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input
        type="text"
        name="_subject"
        placeholder="Subject"
        required>
    <input
        type="text"
        name="name"
        placeholder="Your Name"
        required>
    <input
        type="email"
        name="email"
        placeholder="Your Email Address"
        required>
    <textarea
        name="message"
        placeholder="Tell me about your opportunity, project, or question..."
        required></textarea>
    <input type="text" name="_honey" style="display:none">
    <button type="submit">Send Message</button>
    </form>
    """
    st.header("📩 Contact Me", divider="green")
    st.markdown(contactForm, unsafe_allow_html=True)