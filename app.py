import streamlit as st

st.set_page_config(page_title="Early Access Platform", layout="centered")

# ---------- STYLING ----------
st.markdown("""
<style>
.title { font-size: 36px; font-weight: 700; }
.subtitle { font-size: 16px; color: #555; margin-bottom: 20px; }

.cta {
    display: inline-block;
    padding: 16px 40px;
    background-color: black;
    color: white;
    text-decoration: none;
    border-radius: 8px;
    font-size: 18px;
    font-weight: 600;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
interest = st.text_input("Enter your area of interest")

# ---------- CONTENT ----------
if interest.strip():
    st.markdown(f"<div class='title'>Early Access for {interest}</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Complete your request to join the waitlist</div>", unsafe_allow_html=True)

    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform"

    st.markdown(
        f'<a href="{form_url}" target="_blank" class="cta">Request Invitation</a>',
        unsafe_allow_html=True
    )

else:
    st.markdown("<div class='title'>Early Access Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Enter your interest to continue</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.write("© 2026 Early Access Platform")
