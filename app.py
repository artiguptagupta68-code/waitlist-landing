import streamlit as st
import requests

st.set_page_config(page_title="Early Access Platform", layout="centered")

# ---------- STYLES ----------
st.markdown("""
<style>
.title { font-size: 36px; font-weight: 700; }
.subtitle { font-size: 16px; color: #555; margin-bottom: 20px; }

input, textarea {
    border-radius: 6px !important;
}

button[kind="primary"] {
    background-color: #111 !important;
    border-radius: 6px !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---------- STEP 1: USER INPUT ----------
interest = st.text_input("Enter your area of interest")

# ---------- STEP 2: DYNAMIC HEADER ----------
if interest.strip():
    st.markdown(f"<div class='title'>Apply for {interest}</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Provide your details to request early access</div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='title'>Early Access Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Enter your interest to begin</div>", unsafe_allow_html=True)

# ---------- STEP 3: INTERNAL FORM ----------
if interest.strip():

    with st.form("dynamic_form"):

        name = st.text_input("Full Name")
        email = st.text_input("Email Address")

        submit = st.form_submit_button("Request Invitation")

        if submit:

            # ---------- VALIDATION ----------
            if not name or not email:
                st.error("All fields are required")

            elif "@" not in email:
                st.error("Enter a valid email")

            else:
                # ---------- SEND TO N8N ----------
                webhook_url = "https://your-ngrok-url/webhook/waitlist"  # replace this

                data = {
                    "name": name,
                    "email": email,
                    "interest": interest
                }

                try:
                    res = requests.post(webhook_url, json=data)

                    if res.status_code == 200:
                        st.success("Your request has been submitted successfully")
                    else:
                        st.error("Submission failed. Try again.")

                except:
                    st.error("Could not connect to server")

# ---------- FOOTER ----------
st.markdown("---")
st.write("© 2026 Early Access Platform")
