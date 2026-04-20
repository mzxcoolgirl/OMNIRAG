import requests
import streamlit as st

def generate_answer(context, query, history=""):

    # 🧠 Improved Prompt (better answers)
    prompt = f"""
You are a helpful assistant.

Answer the question using the context below.

Rules:
- Try your best to answer using the context
- If answer is partially available, explain using available info
- Do NOT say "Not found" unless absolutely nothing is relevant



Context:
{context}

Question:
{query}
"""

    # 🔥 Fallback Models (auto-switch if one fails)
    models = [
        "llama-3.1-8b-instant",
        "llama-3.1-70b-versatile",
        "gemma2-9b-it"
    ]

    for model in models:
        try:
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {st.secrets['API_KEY']}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.3  # more accurate answers
                },
                timeout=30
            )

            # ❌ If HTTP error → try next model
            if response.status_code != 200:
                continue

            data = response.json()

            # ❌ If invalid response → try next model
            if "choices" not in data:
                continue

            # ✅ SUCCESS
            return data["choices"][0]["message"]["content"]

        except Exception:
            # ❌ If request fails → try next model
            continue

    # ❌ If all models fail
    return "⚠️ All models failed. Please try again later."