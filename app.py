import streamlit as st
import requests
import re

# ---------- CONFIG ----------
WEBHOOK_URL = "http://localhost:5678/webhook/waitlist"
# If using ngrok, replace with:
# WEBHOOK_URL = "https://your-ngrok-url.ngrok-free.dev/webhook/waitlist"

st.set_page_config(page_title="Early Access Platform", layout="centered")

# ---------- STYLING ----------
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.container {
    background: #ffffff;
    padding: 40px;
    border-radius: 14px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.05);
    max-width: 600px;
    margin: auto;
    margin-top: 60px;
}

.title {
    font-size: 30px;
    font-weight: 700;
    color: #111;
    margin-bottom: 8px;
}

.subtitle {
    font-size: 15px;
    color: #666;
    margin-bottom: 25px;
}

.stTextInput input {
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #ddd;
}

div.stButton > button {
    width: 100%;
    padding: 14px;
    border-radius: 10px;
    background-color: #111;
    color: white;
    font-size: 16px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- VALIDATION ----------
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------- UI ----------
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="title">Early Access Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Request early access tailored to your area of interest.</div>', unsafe_allow_html=True)

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
        st.error("Please enter a valid email address.")

    else:
        payload = {
            "name": name.strip(),
            "email": email.strip(),
            "interest": interest.strip()
        }

        try:
            response = requests.post(
                WEBHOOK_URL,
                json=payload,
                timeout=5
            )

            if response.status_code == 200:
                st.success("Your request has been submitted successfully.")
            else:
                st.error("Submission failed. Please try again.")

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to server. Make sure n8n is running.")

        except requests.exceptions.Timeout:
            st.error("Server timeout. Please try again.")

        except Exception:
            st.error("Unexpected error occurred.")

st.markdown("</div>", unsafe_allow_html=True)
