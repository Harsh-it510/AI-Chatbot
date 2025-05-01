import streamlit as st
from main import get_bot_response

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 AI Chatbot (LLaMA 3.2)")
st.markdown("Ask anything! The chatbot uses LLaMA 3.2 via LangChain and Ollama.")

# Store chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", placeholder="Type your message here...")

if st.button("Send") or user_input:
    if user_input.strip():
        st.session_state.chat_history.append(("You", user_input))
        bot_reply = get_bot_response(user_input)
        st.session_state.chat_history.append(("Bot", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
