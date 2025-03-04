import streamlit as st
import requests
import time
import urllib.parse  # For URL encoding

# ShrinkEarn API details (your key)
API_KEY = "f846b26135aca746c4fdfcd3195a295b96e6027b"
BASE_URL = "https://shrinkearn.com/api"

# App title and description
st.title("Shrink & Earn - Shorten Links, Save Time!")
st.write("Paste your long URL below and get a short, shareable link instantly. Share it anywhere—social media, emails, or chats—and make every click count!")

# Input field for the long URL
long_url = st.text_input("Enter Your Long URL Here", placeholder="e.g., https://example.com")

# Notification option
notify = st.checkbox("Notify me when my link gets clicks (optional)", help="Enter your email below to get updates!")
email = ""
if notify:
    email = st.text_input("Your Email (for notifications)", placeholder="e.g., you@example.com")

# Button to shorten the link
if st.button("Shrink It!"):
    if long_url:
        # API request to ShrinkEarn
        params = {"api": API_KEY, "url": long_url}
        try:
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    short_url = data["shortenedUrl"]
                    st.success(f"Your Short Link: {short_url}")
                    st.write("Share it with one click below!")

                    # Fun animation to engage users
                    with st.spinner("Shrinking your link..."):
                        time.sleep(1)
                    st.balloons()

                    # Notification logic (placeholder)
                    if notify and email:
                        st.write(f"We’ll notify you at {email} when your link gets clicks!")
                        # Add email service here if desired (e.g., SendGrid)

                    # Sharing options with icons (emojis) and links
                    st.subheader("Share Your Link:")
                    encoded_url = urllib.parse.quote(short_url)  # Encode URL for sharing

                    # WhatsApp
                    whatsapp_link = f"https://api.whatsapp.com/send?text=Check%20out%20this%20link:%20{encoded_url}"
                    st.markdown(f"📱 [WhatsApp]({whatsapp_link})", unsafe_allow_html=True)

                    # Twitter (X)
                    twitter_link = f"https://twitter.com/intent/tweet?text=Check%20this%20out:%20{encoded_url}"
                    st.markdown(f"🐦 [Twitter (X)]({twitter_link})", unsafe_allow_html=True)

                    # Facebook
                    facebook_link = f"https://www.facebook.com/sharer/sharer.php?u={encoded_url}"
                    st.markdown(f"📘 [Facebook]({facebook_link})", unsafe_allow_html=True)

                    # Telegram
                    telegram_link = f"https://t.me/share/url?url={encoded_url}&text=Check%20this%20out!"
                    st.markdown(f"✈️ [Telegram]({telegram_link})", unsafe_allow_html=True)

                    # Email
                    email_link = f"mailto:?subject=Check%20this%20out&body=Here’s%20a%20cool%20link:%20{short_url}"
                    st.markdown(f"✉️ [Email]({email_link})", unsafe_allow_html=True)

                else:
                    st.error(f"Error: {data.get('message', 'Unknown issue')}")
            else:
                st.error("Failed to connect to ShrinkEarn. Please try again.")
        except Exception as e:
            st.error(f"Oops! Something went wrong: {str(e)}")
    else:
        st.error("Please enter a URL to shorten!")

# Footer to encourage sharing
st.write("**Pro Tip**: Share your short links with friends or followers to reach more people!")
st.write("Powered by ShrinkEarn - Making links shorter and life easier.")
