import streamlit as st
import openai
from prompts import INITIAL_PROMPT, RULES
from test import TEST_PROMPT
import os

# Show title and description.
st.title("💬 Suremploy Generator")
st.write(
    "Fitness For Work Generator"
)

auth = False
if password := st.text_input("Enter the password", type="password"):
    if password == st.secrets.get('PASSWORD', None):
        auth = True
    else:
        st.error("Invalid password.")


if auth:
    # Ask user for their OpenAI API key via `st.text_input`.
    openai_api_key = st.secrets['OPENAI_KEY']

    # Create an OpenAI client.
    client = openai.OpenAI(api_key=openai_api_key)

    # Create a session state variable to store the chat messages.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message.
    if prompt := st.chat_input("Enter your prompt:"):
        # Format the prompt using the INITIAL_PROMPT and RULES.
        question_prompt = INITIAL_PROMPT.format(
            assessment_details=prompt.replace("\n\n", "\n"),
            gender="Female",
            rules=RULES
        )

        # Store and display the user's input only.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": question_prompt}],
            temperature=0.0
        )

        # Get the response content.
        response_content = completion.choices[0].message.content
        response_content = response_content.replace("Ms X", f"Ms Smith")

        # Display and store the response.
        with st.chat_message("assistant"):
            st.markdown(response_content)
        st.session_state.messages.append({"role": "assistant", "content": response_content})
