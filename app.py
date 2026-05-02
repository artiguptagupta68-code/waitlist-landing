import streamlit as st

st.set_page_config(page_title="Early Access", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 600;
    margin-bottom: 10px;
}
.subtitle {
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}
.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-top: 40px;
}
.card {
    padding: 20px;
    border-radius: 10px;
    background-color: #f9f9f9;
    margin-bottom: 15px;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# ---- HERO SECTION ----
st.markdown('<div class="main-title">Early Access Platform for Data Science Opportunities</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">A curated system designed to help you discover relevant opportunities, build practical skills, and accelerate your career growth.</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    **What you can expect:**

    - Curated job opportunities tailored to your profile  
    - Real-world project exposure  
    - Structured updates to help you stay ahead  
    """)

    if st.button("Request Invitation"):
        st.markdown(
            "[Click here to join the waitlist](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
        )

with col2:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71")

st.markdown("---")

# ---- FEATURES SECTION ----
st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><b>Curated Listings</b><br>Relevant opportunities filtered for quality and relevance.</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><b>Project-Based Learning</b><br>Hands-on projects aligned with industry expectations.</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><b>Continuous Updates</b><br>Stay informed with structured and timely insights.</div>', unsafe_allow_html=True)

st.markdown("---")

# ---- INFORMATION SECTION ----
st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)

st.markdown("""
1. Register your interest using the waitlist form  
2. Get onboarded as part of the early access group  
3. Receive curated updates and opportunities directly  
""")

st.markdown("---")

# ---- FAQ SECTION ----
st.markdown('<div class="section-title">Frequently Asked Questions</div>', unsafe_allow_html=True)

with st.expander("Is there any cost involved?"):
    st.write("Early access is currently free for selected users.")

with st.expander("Who should register?"):
    st.write("Students and professionals interested in data science and related fields.")

with st.expander("When will access be granted?"):
    st.write("Selected users will be notified via email.")

st.markdown("---")

# ---- FINAL CTA ----
st.markdown('<div class="section-title">Request Access</div>', unsafe_allow_html=True)

st.write("Submit your details to be considered for early access.")

if st.button("Join Waitlist"):
    st.markdown(
        "[Submit your details](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
    )

# ---- FOOTER ----
st.markdown('<div class="footer">© 2026 | Early Access Platform</div>', unsafe_allow_html=True)
