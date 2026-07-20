import streamlit as st
from constants import Experience


def experience_unit(title, position, date, location, content, button_name, button_link, expanded=False):
    with st.expander(
        f"🏢 {title} | {position}",
        expanded=expanded):
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader(title)
            st.markdown(f"**{position}**")

        with col2:
            st.markdown(f"**{date}**")
            st.markdown(f"**{location}**")

        st.write(content)
        st.link_button(button_name, button_link)

def experienceTab():
    st.header("📚 Experience", divider="green")

    for i, exp in enumerate(Experience):
        experience_unit(
            exp[0], exp[1], exp[2], exp[3],
            exp[4], exp[5], exp[6],
            expanded=(i == 0) 
        )


