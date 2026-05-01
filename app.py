import streamlit as st

st.set_page_config(page_title="Early Access", layout="wide")

# ---- HERO SECTION ----
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    font-weight:700;
}
.subtext {
    font-size:20px;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🚀 Something Powerful is Coming</p>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Built for students & professionals who want real opportunities</p>', unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
### Why join?

- 🎯 Curated opportunities (not spam)
- 📊 Real-world projects
- 🚀 Faster career growth
""")

    if st.button("👉 Join Waitlist"):
        st.markdown(
            "[Click here to join](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
        )

with col2:
    st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71")

st.markdown("---")

# ---- INTERACTIVE SECTION ----
st.markdown("## 🔍 What will you get?")

tab1, tab2, tab3 = st.tabs(["Jobs", "Projects", "Growth"])

with tab1:
    st.write("Get curated Data Science jobs daily — no noise, only relevant roles.")

with tab2:
    st.write("Hands-on projects that actually build your portfolio.")

with tab3:
    st.write("Guidance, resources, and updates to grow faster.")

st.markdown("---")

# ---- FAQ (Interactive Expanders) ----
st.markdown("## ❓ Frequently Asked Questions")

with st.expander("Is this free?"):
    st.write("Yes, early access is completely free.")

with st.expander("Who is this for?"):
    st.write("Students, job seekers, and professionals in Data Science & tech.")

with st.expander("When will I get access?"):
    st.write("Soon after signup. Early users will be notified first.")

st.markdown("---")

# ---- FINAL CTA ----
st.markdown("## 🔐 Limited Early Access")

st.warning("Only a few early spots available!")

if st.button("🚀 Request Invite Now"):
    st.markdown(
        "[Join the waitlist here](https://docs.google.com/forms/d/e/1FAIpQLSdlPeC5iQCiD22ngyPHS9wOrenztnz-KEyCq1Yz1Yz7nAHYeA/viewform?usp=header)"
    )

st.markdown("---")
st.markdown("⚡ Built with ❤️ using Streamlit")
