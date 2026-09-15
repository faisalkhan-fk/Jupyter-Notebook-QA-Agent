def ask_question(question):
    relevant_chunks = get_relevant_chunks(question)
    context = "\n".join(relevant_chunks)

    prompt = f"""Answer the question based only on the context below.

Context:
{context}

Question:
{question}

Answer:"""

    response = gen_model.generate_content(prompt)

    return "Hello Faisal Khan,\n" + response.text
