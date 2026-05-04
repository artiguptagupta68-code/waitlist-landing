import streamlit as st

st.set_page_config(page_title="Early Access Platform", layout="centered")

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}

.container {
    background-color: white;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.06);
    margin-top: 60px;
}

.title {
    font-size: 34px;
    font-weight: 700;
    color: #111;
    margin-bottom: 10px;
}

.subtitle {
    font-size: 16px;
    color: #666;
    margin-bottom: 30px;
}

.input-label {
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 8px;
    color: #333;
}

.stTextInput > div > div > input {
    border-radius: 8px;
    padding: 12px;
    border: 1px solid #ddd;
}

.cta-button {
    display: inline-block;
    width: 100%;
    text-align: center;
    padding: 16px;
    background-color: #111;
    color: white;
    text-decoration: none;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
    transition: all 0.2s ease;
}

.cta-button:hover {
    background-color: #333;
}

.footer {
    text-align: center;
    font-size: 13px;
    color: #999;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------- MAIN CONTAINER ----------
st.markdown("<div class='container'>", unsafe_allow_html=True)

# ---------- INPUT ----------
st.markdown("<div class='input-label'>Area of Interest</div>", unsafe_allow_html=True)
interest = st.text_input("", placeholder="e.g., Data Science, Finance, Marketing")

# ---------- DYNAMIC CONTENT ----------
if interest.strip():
    st.markdown(
        f"<div class='title'>Early Access for {interest}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Submit your request to receive early access tailored to your domain.</div>",
        unsafe_allow_html=True
    )

    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform"

    st.markdown(
        f'<a href="{form_url}" target="_blank" class="cta-button">Request Invitation</a>',
        unsafe_allow_html=True
    )

else:
    st.markdown(
        "<div class='title'>Early Access Platform</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Enter your area of interest to proceed with your request.</div>",
        unsafe_allow_html=True
    )

# ---------- CLOSE CONTAINER ----------
st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer'>© 2026 Early Access Platform</div>", unsafe_allow_html=True)
