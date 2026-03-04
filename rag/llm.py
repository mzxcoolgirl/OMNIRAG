import ollama


def generate_answer(context, query, history):

    prompt = f"""
    You are a helpful assistant answering questions from a document.

    Use the conversation history and the provided context.

    Conversation History:
    {history}

    Context:
    {context}

    Question:
    {query}

    Answer clearly using the document.
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]