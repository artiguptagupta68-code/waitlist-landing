import streamlit as st
import urllib.parse

st.set_page_config(page_title="Early Access Platform", layout="wide")

# ---------- STYLES ----------
st.markdown("""
<style>
.block-container { max-width: 1100px; padding-top: 2rem; }

.title { font-size: 44px; font-weight: 700; }
.subtitle { font-size: 18px; color: #555; margin-top: 10px; margin-bottom: 30px; }

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
}
</style>
""", unsafe_allow_html=True)

# ---------- INTEREST OPTIONS ----------
options = ["Data Science", "Software Development", "Marketing", "Finance"]

# ---------- GET FROM URL ----------
query_params = st.query_params
url_interest = query_params.get("interest", None)

# Normalize URL value
if url_interest:
    url_interest = url_interest.replace("+", " ")

# ---------- USER INPUT (VISIBLE) ----------
if url_interest in options:
    default_index = options.index(url_interest)
else:
    default_index = 0

interest = st.selectbox(
    "Select your area of interest",
    options,
    index=default_index
)

# ---------- CONTENT ----------
content_map = {
    "Data Science": {
        "title": "Early Access for Data Science Opportunities",
        "desc": "Curated roles, projects, and insights.",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71"
    },
    "Software Development": {
        "title": "Early Access for Developer Opportunities",
        "desc": "Engineering roles and coding projects.",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475"
    },
    "Marketing": {
        "title": "Early Access for Marketing Opportunities",
        "desc": "Campaigns, growth, and strategy insights.",
        "image": "https://images.unsplash.com/photo-1557838923-2985c318be48"
    },
    "Finance": {
        "title": "Early Access for Finance Opportunities",
        "desc": "Market insights and finance roles.",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f"
    }
}

selected = content_map[interest]

# ---------- FORM LINK ----------
base_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform"
encoded_interest = urllib.parse.quote(interest)

form_link = f"{base_form_url}?usp=pp_url&entry.123456={encoded_interest}"

# ---------- HERO ----------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown(f"<div class='title'>{selected['title']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='subtitle'>{selected['desc']}</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="cta-container">
        <a class="cta-button" href="{form_link}" target="_blank">
            Request Invitation
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image(selected["image"], use_container_width=True)

# ---------- FOOTER ----------
st.markdown("<hr>")
st.write("© 2026 Early Access Platform")
