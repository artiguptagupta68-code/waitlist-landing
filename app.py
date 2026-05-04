import streamlit as st
import urllib.parse

st.set_page_config(page_title="Early Access Platform", layout="wide")

# ---------- INTEREST OPTIONS ----------
options = ["Data Science", "Software Development", "Marketing", "Finance"]

# ---------- SESSION STATE ----------
if "interest" not in st.session_state:
    st.session_state.interest = None

# ---------- ENTRY SCREEN ----------
if st.session_state.interest is None:

    st.markdown("<h2 style='text-align:center;'>Select Your Area of Interest</h2>", unsafe_allow_html=True)

    interest = st.selectbox(
        "Choose your domain",
        options
    )

    if st.button("Continue"):
        st.session_state.interest = interest
        st.rerun()

    st.stop()
