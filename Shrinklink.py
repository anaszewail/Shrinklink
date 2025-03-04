import streamlit as st
import requests
import time

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
                    st.write("Share this link anywhere—every click helps spread the word!")
                    
                    # Fun animation to engage users
                    with st.spinner("Shrinking your link..."):
                        time.sleep(1)
                    st.balloons()

                    # Notification logic (simplified for demo)
                    if notify and email:
                        st.write(f"We’ll notify you at {email} when your link gets clicks!")
                        # In a real app, you'd integrate an email service like SMTP or a third-party API (e.g., SendGrid) here

                else:
                    st.error(f"Error: {data.get('message', 'Unknown issue')}")
            else:
                st.error("Failed to connect to ShrinkEarn. Please try again.")
        except Exception as e:
            st.error(f"Oops! Something went wrong: {str(e)}")
    else:
        st.error("Please enter a URL to shorten!")

# Footer to encourage sharing
st.write("**Pro Tip**: Share your short links on Twitter, WhatsApp, or forums to reach more people!")
st.write("Powered by ShrinkEarn - Making links shorter and life easier.")
