import streamlit as st

st.set_page_config(page_title="Waitlist", layout="centered")

st.title("🚀 Something Big is Coming")
st.write("We’re building something exciting. Get early access.")
st.write("Join the waitlist to receive your invitation.")

st.markdown("## 🔐 Request Invite")

st.link_button(
    "Join Waitlist 🚀",
    "https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform"
)