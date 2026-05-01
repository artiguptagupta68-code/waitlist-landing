import streamlit as st

# Page config
st.set_page_config(page_title="Early Access", layout="centered")

# Hero Section
st.markdown("""
# 🚀 Get Early Access to Something Powerful

### Built for students & professionals looking for **real opportunities**

We’re creating a platform that helps you:
- 🎯 Discover curated opportunities
- 📊 Work on real-world projects
- 🚀 Grow faster in your career

---

## 🔐 Join the Waitlist

Be among the **first users** to get access.

""")

# CTA Button
if st.button("👉 Request Invite"):
    st.markdown(
        "[Click here to join the waitlist](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
    )

# Footer
st.markdown("---")
st.markdown("⚡ Limited early access. Don’t miss out.")
