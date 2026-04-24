import streamlit as st
from db import init_db, save_chat
from memory import build_memory
from llm import get_response

init_db()

st.set_page_config(page_title="Mini GPT Chatbot")

st.title("🤖 Mini GPT Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]

user_input=st.text_input("Ask something:")

if st.button("Send") and user_input:

    memory=build_memory()

    prompt=f"""
You are a helpful AI assistant.

Conversation history:
{memory}

User: {user_input}
AI:
"""

    with st.spinner("Thinking..."):
        reply=get_response(prompt)

    save_chat(user_input,reply)

    st.session_state.messages.append(
        ("You",user_input)
    )

    st.session_state.messages.append(
        ("Bot",reply)
    )


for role,msg in st.session_state.messages:

    if role=="You":
        st.write(f"🧑 {msg}")
    else:
        st.write(f"🤖 {msg}")