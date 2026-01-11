import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

with st.sidebar:
    openai_api_key = os.getenv('OPENAI_API_KEY')
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/lim-examples/blob/main/Chatbot.py)"
    "[![Open in Github Codespaces](https://github.com/codespacesbadget.svg)](https://codespaces.net/streamlit/lim-exampes?quickstart=1)"

st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.session_state["message"] = [{"role": "assistant", "content":"How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
# Accept user input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop

    client = OpenAI(api_key=openai_api_key)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-4o", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role":"assistant", "content": msg}
    )
    st.chat_message("assistant").write(msg)
    