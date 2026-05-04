import streamlit as st
import urllib.parse

st.set_page_config(page_title="Early Access Platform", layout="wide")

# ---------- STYLES ----------
st.markdown("""
<style>
.block-container { max-width: 1100px; padding-top: 2rem; }

.title { font-size: 44px; font-weight: 700; }
.subtitle { font-size: 18px; color: #555; margin-top: 10px; margin-bottom: 30px; }

.section-title { font-size: 26px; font-weight: 600; margin-top: 50px; }

.cta-container { text-align: center; margin-top: 30px; }

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

.disabled-button {
    display:inline-block;
    padding:20px 50px;
    font-size:20px;
    font-weight:600;
    color:#aaa;
    background:#ddd;
    border-radius:10px;
    cursor:not-allowed;
}

.card {
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #eee;
    background-color: #fafafa;
}

.footer {
    text-align: center;
    font-size: 14px;
    color: #888;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)

# ---------- USER INPUT ----------
user_input = st.text_input("Enter your area of interest")

# ---------- NORMALIZATION FUNCTION ----------
def detect_interest(text):
    if not text:
        return "General"

    text = text.lower()

    if any(k in text for k in ["data", "ml", "ai"]):
        return "Data Science"
    elif any(k in text for k in ["dev", "software", "coding"]):
        return "Software Development"
    elif any(k in text for k in ["market", "growth"]):
        return "Marketing"
    elif any(k in text for k in ["finance", "stock"]):
        return "Finance"
    else:
        return "General"

interest = detect_interest(user_input)

# ---------- CONTENT MAP ----------
content_map = {
    "Data Science": {
        "title": "Early Access for Data Science Opportunities",
        "desc": "Curated roles, real-world projects, and structured updates.",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71"
    },
    "Software Development": {
        "title": "Early Access for Developer Opportunities",
        "desc": "Engineering roles, coding projects, and technical insights.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475"
    },
    "Marketing": {
        "title": "Early Access for Marketing Opportunities",
        "desc": "Campaigns, growth strategies, and real-world exposure.",
        "image": "https://images.unsplash.com/photo-1557838923-2985c318be48"
    },
    "Finance": {
        "title": "Early Access for Finance Opportunities",
        "desc": "Market insights, financial roles, and domain updates.",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f"
    },
    "General": {
        "title": "Early Access Platform",
        "desc": "Explore opportunities across multiple domains.",
        "image": "https://images.unsplash.com/photo-1492724441997-5dc865305da7"
    }
}

selected = content_map[interest]

# ---------- FORM LINK ----------
base_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform"

encoded_interest = urllib.parse.quote(user_input if user_input else interest)

# ⚠️ Replace entry.123456 with your actual Google Form field ID
form_link = f"{base_form_url}?usp=pp_url&entry.123456={encoded_interest}"

# ---------- HERO SECTION ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(f"<div class='title'>{selected['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{selected['desc']}</div>", unsafe_allow_html=True)

    # CTA BUTTON LOGIC
    if user_input.strip() == "":
        st.markdown("""
        <div class="cta-container">
            <div class="disabled-button">
                Request Invitation
            </div>
            <p style="color:#888; font-size:14px; margin-top:10px;">
                Enter your area of interest to continue
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="cta-container">
            <a class="cta-button" href="{form_link}" target="_blank">
                Request Invitation
            </a>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.image(selected["image"], use_container_width=True)

# ---------- FEATURES ----------
st.markdown("<div class='section-title'>Key Features</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'><b>Curated Listings</b><br><br>Relevant opportunities across domains.</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><b>Practical Exposure</b><br><br>Real-world project-based learning.</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'><b>Continuous Updates</b><br><br>Stay informed with structured insights.</div>", unsafe_allow_html=True)

# ---------- FINAL CTA ----------
st.markdown("<div class='section-title'>Request Access</div>", unsafe_allow_html=True)

if user_input.strip() != "":
    st.markdown(f"""
    <div class="cta-container">
        <a class="cta-button" href="{form_link}" target="_blank">
            Join Waitlist
        </a>
    </div>
    """, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("<div class='footer'>© 2026 Early Access Platform</div>", unsafe_allow_html=True)
