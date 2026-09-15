def get_relevant_chunks(question, k=3):
    q_embedding = model.encode([question])                        # create a vector for the question
    distances, indices = index.search(np.array(q_embedding), k)   # find the top-k most similar chunks
    return [chunks[i] for i in indices[0]]                        # return their text
