import streamlit as st
import requests
import re

# -----------------------
# CONFIG
# -----------------------
WEBHOOK_URL = "http://localhost:5678/webhook/waitlist"

# -----------------------
# UI
# -----------------------
st.set_page_config(page_title="Waitlist Form", page_icon="🚀")
st.title("🚀 Join the Waitlist")

st.write("Fill in your details below:")

# -----------------------
# INPUT FIELDS
# -----------------------
name = st.text_input("Name")
email = st.text_input("Email")
interest = st.text_input("Area of Interest")

# -----------------------
# EMAIL VALIDATION
# -----------------------
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

# -----------------------
# SUBMIT BUTTON
# -----------------------
if st.button("Submit"):

    # Validation
    if not name or not email or not interest:
        st.warning("⚠️ Please fill all fields")
    
    elif not is_valid_email(email):
        st.warning("⚠️ Please enter a valid email address")

    else:
        payload = {
            "name": name,
            "email": email,
            "interest": interest
        }

        with st.spinner("Submitting..."):
            try:
                response = requests.post(
                    WEBHOOK_URL,
                    json=payload,
                    timeout=10
                )

                # -----------------------
                # RESPONSE HANDLING
                # -----------------------
                if response.status_code == 200:

                    st.success("✅ Successfully submitted!")

                    # Try parsing JSON safely
                    try:
                        data = response.json()
                        st.json(data)
                    except:
                        st.info("ℹ️ Submitted successfully (no JSON response returned)")
                        st.text(response.text)

                else:
                    st.error(f"❌ Server error ({response.status_code})")
                    st.text(response.text)

            except requests.exceptions.Timeout:
                st.error("⏳ Request timed out. Please try again.")

            except requests.exceptions.ConnectionError:
                st.error("🔌 Could not connect to server. Is n8n running?")

            except Exception as e:
                st.error(f"❌ Unexpected error: {str(e)}")
