import numpy as np
from rank_bm25 import BM25Okapi

class HybridRetriever:
    def __init__(self, chunks, embeddings, index):
        self.chunks = chunks
        self.index = index
        self.tokenized_chunks = [chunk.lower().split() for chunk in chunks]
        self.bm25 = BM25Okapi(self.tokenized_chunks)

    def search(self, query_embedding, query, k=10):

        # ✅ FIX FAISS SHAPE
        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)
        vector_results = [self.chunks[i] for i in indices[0]]

        # ✅ BM25 (keyword search)
        tokenized_query = query.lower().split()
        bm25_scores = self.bm25.get_scores(tokenized_query)

        bm25_indices = np.argsort(bm25_scores)[::-1][:k]
        keyword_results = [self.chunks[i] for i in bm25_indices]

        # 🔥 FILTER keyword results (important)
        filtered_keywords = []
        for chunk in keyword_results:
            if any(word in chunk.lower() for word in tokenized_query):
                filtered_keywords.append(chunk)

        if filtered_keywords:
            keyword_results = filtered_keywords

        # 🔥 PRIORITY: keyword > vector
        combined = keyword_results + vector_results

        # 🔥 REMOVE duplicates
        seen = set()
        unique_results = []

        for chunk in combined:
            if chunk not in seen:
                unique_results.append(chunk)
                seen.add(chunk)

        return unique_results[:k]