import faiss
import numpy as np

class VectorStore:
  def __init__(self, dim: int = 1536):
    self.index = faiss.IndexFlatL2(dim)
    self.vectors = []
    self.metadatas = []

    def add(self, vector: np.ndarray, metadata: dict):
      self.index.add(vector[np.newaxis, :])
      self.vectors.append(vector)
      self.metadatas.append(metadata)

    def search(self, query_vector: np.ndarray, k: int = 5):
      D, I = self.index.search(query_vector[np.newaxis, :], k)
      return [(self.metadatas[i], D[0][j]) for j, i in enumerate(I[0])]