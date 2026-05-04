import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import re

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Early Access Platform", layout="centered")

# ---------- STYLING ----------
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}

.container {
    background: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.05);
    margin-top: 60px;
}

.title {
    font-size: 32px;
    font-weight: 700;
    color: #111;
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

.submit-btn button {
    width: 100%;
    padding: 14px;
    border-radius: 10px;
    background-color: black;
    color: white;
    font-weight: 600;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------- GOOGLE SHEETS SETUP ----------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key("1QNd4f-LTV8qurUgVdTVl543iw5FcrKAQtLdhmQsFYVk").sheet1

# ---------- UI ----------
st.markdown("<div class='container'>", unsafe_allow_html=True)

st.markdown("<div class='title'>Early Access Platform</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Submit your details to request early access tailored to your domain.</div>", unsafe_allow_html=True)

# ---------- FORM ----------
with st.form("waitlist_form"):

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    interest = st.text_input("Area of Interest")

    submit = st.form_submit_button("Request Invitation")

# ---------- VALIDATION ----------
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------- SUBMIT LOGIC ----------
if submit:
    if not name or not email or not interest:
        st.error("All fields are required.")
    
    elif not is_valid_email(email):
        st.error("Please enter a valid email address.")
    
    else:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            sheet.append_row([name, email, interest, timestamp])

            st.success("Your request has been submitted successfully.")

        except Exception as e:
            st.error("Submission failed. Please try again.")

st.markdown("</div>", unsafe_allow_html=True)
