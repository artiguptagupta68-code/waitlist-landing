import streamlit as st
import urllib.parse

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Early Access Platform",
    layout="centered"
)

# ---------- STYLES ----------
st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 10px;
}

.sub-text {
    font-size: 16px;
    color: #555;
    margin-bottom: 30px;
}

.input-box input {
    border-radius: 6px;
    padding: 10px;
}

.cta-button {
    display: inline-block;
    padding: 16px 36px;
    background-color: #111;
    color: white;
    text-decoration: none;
    border-radius: 8px;
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
}

.cta-button:hover {
    background-color: #333;
}

.footer {
    margin-top: 60px;
    text-align: center;
    font-size: 13px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# ---------- USER INPUT ----------
interest = st.text_input("Enter your area of interest")

# ---------- DYNAMIC CONTENT ----------
if interest.strip():
    st.markdown(f"<div class='main-title'>Early Access for {interest}</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>Submit your request to join the early access list.</div>", unsafe_allow_html=True)

    # ---------- GOOGLE FORM PREFILL ----------
    encoded_interest = urllib.parse.quote(interest)

    form_url = f"https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?usp=pp_url&entry.123456={encoded_interest}"

    # ---------- CTA BUTTON ----------
    st.markdown(
        f'<a href="{form_url}" target="_blank" class="cta-button">Request Invitation</a>',
        unsafe_allow_html=True
    )

else:
    st.markdown("<div class='main-title'>Early Access Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>Enter your interest to continue.</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer'>© 2026 Early Access Platform</div>", unsafe_allow_html=True)
