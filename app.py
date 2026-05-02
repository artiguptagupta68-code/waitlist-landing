import streamlit as st

st.set_page_config(page_title="Early Access", layout="wide")

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>
body {
    background-color: #ffffff;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Typography */
.title {
    font-size: 44px;
    font-weight: 700;
    line-height: 1.2;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-top: 10px;
    margin-bottom: 30px;
}

/* Section titles */
.section-title {
    font-size: 28px;
    font-weight: 600;
    margin-top: 50px;
    margin-bottom: 20px;
}

/* Cards */
.card {
    padding: 25px;
    border-radius: 10px;
    border: 1px solid #eee;
    background-color: #fafafa;
    transition: 0.3s;
}
.card:hover {
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
}

/* Button */
div.stButton > button {
    width: 100%;
    height: 60px;
    font-size: 18px;
    font-weight: 600;
    background-color: #111;
    color: white;
    border-radius: 8px;
    border: none;
}
div.stButton > button:hover {
    background-color: #333;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #888;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="title">Early Access Platform for Data Science Opportunities</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">A focused system designed to help you discover relevant opportunities, gain practical exposure, and accelerate your career.</div>', unsafe_allow_html=True)

    st.markdown("""
    - Curated job opportunities  
    - Real-world project exposure  
    - Structured career updates  
    """)

    if st.button("Request Invitation"):
        st.markdown(
            "[Join the waitlist](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
        )

with col2:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71", use_container_width=True)

st.markdown("---")

# ---------- FEATURES ----------
st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><b>Curated Listings</b><br><br>Opportunities filtered for relevance and quality.</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><b>Project-Based Learning</b><br><br>Hands-on experience aligned with industry expectations.</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><b>Continuous Updates</b><br><br>Timely insights to keep you ahead.</div>', unsafe_allow_html=True)

# ---------- HOW IT WORKS ----------
st.markdown('<div class="section-title">How It Works</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">1. Register your interest</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">2. Get selected for early access</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">3. Receive curated updates</div>', unsafe_allow_html=True)

# ---------- FAQ ----------
st.markdown('<div class="section-title">Frequently Asked Questions</div>', unsafe_allow_html=True)

with st.expander("Is there any cost involved?"):
    st.write("Early access is currently free for selected users.")

with st.expander("Who should register?"):
    st.write("Students and professionals interested in data science and related fields.")

with st.expander("When will access be granted?"):
    st.write("Selected users will be notified via email.")

# ---------- FINAL CTA ----------
st.markdown('<div class="section-title">Request Access</div>', unsafe_allow_html=True)

st.write("Submit your details to be considered for early access.")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    if st.button("Join Waitlist"):
        st.markdown(
            "[Submit your details](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
        )

# ---------- FOOTER ----------
st.markdown('<div class="footer">© 2026 Early Access Platform</div>', unsafe_allow_html=True)
