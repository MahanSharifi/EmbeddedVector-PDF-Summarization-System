from sentence_transformers import SentenceTransformer
import chromadb

class EmbeddingManager:
    def __init__(self, api_key=None):  # api_key is no longer needed
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # lightweight, fast model
        self.client = chromadb.PersistentClient(path="./chroma_db")
    
    def create_collection(self, name="pdf_collection"):
        try:
            collection = self.client.get_collection(name)
        except:
            collection = self.client.create_collection(name)
        return collection
    
    def add_documents(self, collection, documents, ids=None):
        if ids is None:
            ids = [str(i) for i in range(len(documents))]
        
        # Get embeddings using sentence-transformers
        embeddings = self.model.encode(documents).tolist()
        
        collection.add(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )
        return embeddings