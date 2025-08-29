import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="FMCC Chatbot", page_icon="🤖", layout="centered")

# Title and header
st.title("🤖 FMCC AI Chat Assistant")
st.markdown("Welcome to the Fort McMurray Chamber of Commerce Chatbot. Ask me anything about FMCC, local businesses, events, or memberships!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! 👋 I'm the FMCC Assistant. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask a question about the Chamber, business resources, or local events...")

# Mock AI response (replace this with actual GPT later)
def get_ai_response(user_prompt):
    if "membership" in user_prompt.lower():
        return "You can become a member by visiting [fortmcmurraychamber.ca/membership](https://fortmcmurraychamber.ca/membership). We offer multiple tiers with great benefits!"
    elif "event" in user_prompt.lower():
        return "Check out our latest events on [our events page](https://fortmcmurraychamber.ca/events) or subscribe to our newsletter."
    elif "contact" in user_prompt.lower():
        return "You can reach us at info@fortmcmurraychamber.ca or call (780) 743‑3100."
    else:
        return "Thanks for your question! One of our team members will get back to you shortly, or you can email info@fortmcmurraychamber.ca."

# Handle new prompt
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_ai_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
# Full chatbot code to be inserted here.
