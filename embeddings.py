from sentence_transformers import SentenceTransformer

class Embeddings:
    def __init__(self):
        self.model = SentenceTransformer("all-mpnet-base-v2")  # 384-d embeddings

    def get_embeddings(self, text: str):
        return self.model.encode(text)

