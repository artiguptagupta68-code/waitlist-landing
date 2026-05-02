import streamlit as st
import urllib.parse

st.set_page_config(page_title="Early Access Platform", layout="wide")

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}

.title {
    font-size: 44px;
    font-weight: 700;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-top: 10px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 26px;
    font-weight: 600;
    margin-top: 50px;
    margin-bottom: 20px;
}

.card {
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #eee;
    background-color: #fafafa;
    transition: 0.3s;
}
.card:hover {
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

.cta-container {
    text-align: center;
    margin-top: 30px;
}

.cta-button {
    display: inline-block;
    padding: 18px 45px;
    font-size: 18px;
    font-weight: 600;
    color: white;
    background: linear-gradient(90deg, #111, #333);
    border-radius: 8px;
    text-decoration: none;
}

.footer {
    text-align: center;
    font-size: 14px;
    color: #888;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ---------- INTEREST SELECTION ----------
interest = st.selectbox(
    "Select your area of interest",
    ["Data Science", "Software Development", "Marketing", "Finance"]
)

# ---------- DYNAMIC CONTENT ----------
content_map = {
    "Data Science": {
        "title": "Early Access for Data Science Opportunities",
        "desc": "Curated roles, real-world projects, and structured updates tailored for data professionals."
    },
    "Software Development": {
        "title": "Early Access for Software Development Opportunities",
        "desc": "Engineering roles, coding projects, and industry-focused technical updates."
    },
    "Marketing": {
        "title": "Early Access for Marketing Opportunities",
        "desc": "Campaign strategies, growth insights, and real-world marketing exposure."
    },
    "Finance": {
        "title": "Early Access for Finance Opportunities",
        "desc": "Financial roles, market insights, and domain-specific learning resources."
    }
}

selected = content_map[interest]

# ---------- HERO SECTION ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(f"<div class='title'>{selected['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{selected['desc']}</div>", unsafe_allow_html=True)

    st.markdown("""
    - Curated opportunities  
    - Practical exposure  
    - Continuous updates  
    """)

    # FORM LINK (PASSING INTEREST)
    base_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform"
    encoded_interest = urllib.parse.quote(interest)

    form_link = f"{base_form_url}?usp=pp_url&entry.123456={encoded_interest}"

    st.markdown(f"""
    <div class="cta-container">
        <a class="cta-button" href="{form_link}" target="_blank">
            Request Invitation
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71", use_container_width=True)

# ---------- FEATURES ----------
st.markdown("<div class='section-title'>Key Features</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'><b>Curated Listings</b><br><br>Filtered opportunities based on relevance.</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><b>Project-Based Learning</b><br><br>Hands-on experience aligned with industry.</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'><b>Continuous Updates</b><br><br>Stay informed with structured insights.</div>", unsafe_allow_html=True)

# ---------- HOW IT WORKS ----------
st.markdown("<div class='section-title'>How It Works</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>1. Select your interest</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>2. Register via the form</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'>3. Receive tailored updates</div>", unsafe_allow_html=True)

# ---------- FAQ ----------
st.markdown("<div class='section-title'>Frequently Asked Questions</div>", unsafe_allow_html=True)

with st.expander("Is there any cost involved?"):
    st.write("Early access is currently free.")

with st.expander("Who is this for?"):
    st.write("Students and professionals across different domains.")

with st.expander("How will I receive updates?"):
    st.write("Updates will be shared via email.")

# ---------- FINAL CTA ----------
st.markdown("<div class='section-title'>Request Access</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class="cta-container">
    <a class="cta-button" href="{form_link}" target="_blank">
        Join Waitlist
    </a>
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer'>© 2026 Early Access Platform</div>", unsafe_allow_html=True)
