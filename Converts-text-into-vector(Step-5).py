# Load a model that converts text into vectors (numbers)
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)   # create a vector for each chunk
