import requests

def generate_answer(context, query, history=""):

    prompt = f"""
You are an expert assistant.

Give a detailed answer using only the context.

Context:
{context}

Question:
{query}
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": "Bearer YOUR_API_KEY",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()["choices"][0]["message"]["content"]