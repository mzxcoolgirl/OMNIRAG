import requests
import streamlit as st

def generate_answer(context, query, history=""):

    prompt = f"""
You are an expert assistant.

Answer ONLY using the context below.

Context:
{context}

Question:
{query}
"""

    try:
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {st.secrets['API_KEY']}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama3-8b-8192",
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )

        # 🔍 DEBUG (visible in Streamlit)
        st.write("API Response:", response.json())

        # ❌ HTTP error check
        if response.status_code != 200:
            return f"❌ HTTP Error {response.status_code}: {response.text}"

        data = response.json()

        # ❌ API structure error
        if "choices" not in data:
            return f"⚠️ API Error: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"🚨 Exception: {str(e)}"