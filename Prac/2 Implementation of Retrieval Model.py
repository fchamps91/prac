from sklearn.feature_extraction.text import TfidfVectorizer
def build_index(documents):
    index = {}
    for doc_id, text in documents.items():
        for word in set(text.lower().split()):
            if word not in index:
                index[word] = []
            index[word].append(doc_id)
    return index
def boolean_search(index, documents, query):
    words = query.lower().split()
    result = set(documents.keys())
    op = "and"
    for word in words:
        if word in ["and", "or", "not"]:
            op = word
        elif op == "and":
            result &= set(index.get(word, []))
        elif op == "or":
            result |= set(index.get(word, []))
        else:
            result -= set(index.get(word, []))
    return result
def vector_search(documents, query):
    vectorizer = TfidfVectorizer()
    doc_ids = list(documents.keys())
    matrix = vectorizer.fit_transform(documents.values())
    query_vector = vectorizer.transform([query])
    scores = (matrix * query_vector.T).toarray().flatten()
    return sorted(zip(doc_ids, scores), key=lambda x: x[1], reverse=True)
documents = {
    1: "Web content extraction involves retrieving structured data",
    2: "Search engines use document indexing for efficient retrieval",
    3: "Document retrieval is important in web mining applications",
    4: "Indexing helps in retrieving relevant documents based on query terms"
}
index = build_index(documents)
print("Boolean Retrieval Results")
for query in ["retrieval and document", "document or indexing", "retrieval not indexing"]:
    print(f"Query: {query} -> {sorted(boolean_search(index, documents, query))}")
print("\nVector Space Model Results")
for query in ["document retrieval", "web mining", "structured data"]:
    result = [(doc, round(score, 4)) for doc, score in vector_search(documents, query) if score > 0]
    print(f"Query: {query} -> {result}")