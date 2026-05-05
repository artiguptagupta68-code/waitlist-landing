import streamlit as st
import requests
import re

# ---------- CONFIG ----------
WEBHOOK_URL = "https://endorphin-camping-quote.ngrok-free.dev/webhook/waitlist"

st.set_page_config(
    page_title="Early Access Platform",
    layout="centered"
)

# ---------- STYLING ----------
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}

.container {
    background: white;
    padding: 3rem;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06);
    max-width: 650px;
    margin: auto;
    margin-top: 50px;
}

.title {
    font-size: 32px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 15px;
    color: #6b7280;
    margin-bottom: 25px;
}

.stTextInput input {
    border-radius: 10px;
    padding: 12px;
    border: 1px solid #d1d5db;
}

div.stButton > button {
    width: 100%;
    background-color: black;
    color: white;
    padding: 14px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------- VALIDATION ----------
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------- UI ----------
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="title">Early Access Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Submit your details to request early access tailored to your interest.</div>', unsafe_allow_html=True)

# ---------- FORM ----------
with st.form("waitlist_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    interest = st.text_input("Area of Interest")

    submit = st.form_submit_button("Request Invitation")

# ---------- SUBMIT ----------
if submit:
    if not name or not email or not interest:
        st.error("All fields are required.")

    elif not is_valid_email(email):
        st.error("Enter a valid email address.")

    else:
        payload = {
            "name": name,
            "email": email,
            "interest": interest
        }

        try:
            response = requests.post(WEBHOOK_URL, json=payload)

            if response.status_code == 200:
                st.success("Request submitted successfully.")
            else:
                st.error("Submission failed. Try again.")

        except Exception:
            st.error("Server connection failed. Please try later.")

st.markdown("</div>", unsafe_allow_html=True)
