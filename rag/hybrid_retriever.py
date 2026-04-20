from rank_bm25 import BM25Okapi
import numpy as np


class HybridRetriever:

    def __init__(self, chunks, embeddings, index):
        self.chunks = chunks
        self.embeddings = embeddings
        self.index = index

        # Prepare BM25
        tokenized_chunks = [chunk.split(" ") for chunk in chunks]
        self.bm25 = BM25Okapi(tokenized_chunks)

    def search(self, query_embedding, query, k=10):

        # ✅ FIX SHAPE
        query_embedding = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_embedding, k)

        vector_results = [self.chunks[i] for i in indices[0]]

        # keyword (BM25)
        tokenized_query = query.split(" ")
        bm25_scores = self.bm25.get_scores(tokenized_query)

        bm25_indices = np.argsort(bm25_scores)[::-1][:k]
        keyword_results = [self.chunks[i] for i in bm25_indices]

        # combine
        combined = vector_results + keyword_results

        return combined