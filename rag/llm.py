import ollama

def generate_answer(context, query, history=""):

    prompt = f"""
You are an expert assistant.

Your task is to give a DETAILED, LONG, and WELL-EXPLAINED answer based ONLY on the provided context.

Instructions:
- Explain step by step
- Give full understanding
- Use simple language
- Include important details
- If possible, expand the explanation clearly
- Do NOT give short answers

Context:
{context}

Conversation History:
{history}

Question:
{query}

Answer (in detailed paragraph form):
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]