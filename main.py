import streamlit as st
import random
import time
import backend
# Ensure session state is initialized
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'chat'

# Define the target URL
back_url = "http://127.0.0.1:5173/"  # Replace with your desired link

# Create a "Back" button that redirects to the link
st.markdown(f"""
    <a href="{back_url}" target="_self" style="text-decoration: none;">
        <button style="
            background-color: #f44336;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;">
            Back
        </button>
    </a>
""", unsafe_allow_html=True)
# Streamed response emulator
def response_generator(prompt):
    response = backend.GenerateResponse(prompt)
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Career Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! Welcome to Career Bot. How can I assist you today?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Enter your Query"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})