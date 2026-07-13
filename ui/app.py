import streamlit as st
import requests

st.title("Sangturiya Assistant")

user_input = st.text_input("Ask a question:")

if st.button("Send"):
    if user_input:
        # Example of calling the backend which then uses the agent
        # response = requests.post("http://localhost:8000/api/chat", json={"query": user_input})
        # st.write(response.json()["answer"])

        st.write(f"Simulated response to: {user_input}")
    else:
        st.warning("Please enter a question.")
