import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
)

st.title("🚗 Automotive Hardware AI Copilot")

question = st.text_area("Ask your question")

if st.button("Ask AI"):

    response = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    st.write(response.choices[0].message.content)