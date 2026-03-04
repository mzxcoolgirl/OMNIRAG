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

    def search(self, query_embedding, query, k=8):

        # Vector search
        distances, indices = self.index.search(np.array(query_embedding), k)

        vector_results = [self.chunks[i] for i in indices[0]]

        # Keyword search
        tokenized_query = query.split(" ")
        bm25_scores = self.bm25.get_scores(tokenized_query)

        bm25_indices = np.argsort(bm25_scores)[::-1][:k]

        keyword_results = [self.chunks[i] for i in bm25_indices]

        # Combine results
        combined = list(set(vector_results + keyword_results))

        return combined[:k]