import faiss
import numpy as np

def build_index(embeddings):
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    return index


def search(query_embedding, index, chunks, k=3):
    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    return [chunks[i] for i in indices[0]]