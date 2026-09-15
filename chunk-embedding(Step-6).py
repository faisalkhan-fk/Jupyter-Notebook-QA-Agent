# FAISS is a fast tool for finding similar vectors
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)   # simple distance-based search index
index.add(np.array(embeddings))        # add all chunk embeddings to the index
