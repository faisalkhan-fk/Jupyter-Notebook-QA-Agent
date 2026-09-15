# The whole text can't be processed at once, so we split it into smaller chunks
def chunk_text(text, chunk_size=300):
    words = text.split()           # split text into words
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])   # group every 300 words together
        chunks.append(chunk)
    return chunks

chunks = chunk_text(text)
print(len(chunks), "chunks created")
