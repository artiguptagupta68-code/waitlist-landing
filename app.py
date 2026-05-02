import streamlit as st

st.set_page_config(page_title="Early Access", layout="wide")

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>

/* Layout */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1100px;
}

/* Typography */
.title {
    font-size: 46px;
    font-weight: 700;
    line-height: 1.2;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-top: 12px;
    margin-bottom: 30px;
}

/* Section Titles */
.section-title {
    font-size: 28px;
    font-weight: 600;
    margin-top: 60px;
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
    box-shadow: 0px 8px 24px rgba(0,0,0,0.08);
}

/* CTA Button */
.cta-container {
    text-align: center;
    margin-top: 30px;
}

.cta-button {
    display: inline-block;
    padding: 20px 50px;
    font-size: 20px;
    font-weight: 600;
    color: white;
    background: linear-gradient(90deg, #111, #333);
    border-radius: 10px;
    text-decoration: none;
    transition: 0.3s;
}

.cta-button:hover {
    background: linear-gradient(90deg, #000, #222);
    transform: scale(1.04);
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #888;
    margin-top: 80px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO SECTION ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="title">Early Access Platform for Data Science Opportunities</div>', unsafe_allow_html=True)

    st.markdown('<div class="subtitle">A focused system designed to help you discover relevant opportunities, gain practical exposure, and accelerate your career growth.</div>', unsafe_allow_html=True)

    st.markdown("""
    - Curated job opportunities  
    - Real-world project exposure  
    - Structured career updates  
    """)

    st.markdown("""
    <div class="cta-container">
        <a class="cta-button" href="https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header" target="_blank">
            Request Invitation
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71", use_container_width=True)

# ---------- FEATURES ----------
st.markdown('<div class="section-title">Key Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card"><b>Curated Listings</b><br><br>Opportunities filtered for quality and relevance.</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><b>Project-Based Learning</b><br><br>Hands-on experience aligned with industry expectations.</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><b>Continuous Updates</b><br><br>Stay informed with structured insights.</div>', unsafe_allow_html=True)

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

st.markdown("""
<div class="cta-container">
    <a class="cta-button" href="https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header" target="_blank">
        Join Waitlist
    </a>
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown('<div class="footer">© 2026 Early Access Platform</div>', unsafe_allow_html=True)
