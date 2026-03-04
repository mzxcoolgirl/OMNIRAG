from sentence_transformers import CrossEncoder

# load reranker model
reranker_model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, chunks, top_k=3):

    pairs = [(query, chunk) for chunk in chunks]

    scores = reranker_model.predict(pairs)

    scored_chunks = list(zip(chunks, scores))

    scored_chunks.sort(key=lambda x: x[1], reverse=True)

    best_chunks = [chunk for chunk, score in scored_chunks[:top_k]]

    return best_chunks