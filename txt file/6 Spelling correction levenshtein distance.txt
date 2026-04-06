from collections import defaultdict
class IR:
    def __init__(self, docs):
        self.docs = docs
        self.index = defaultdict(set)
        self.vocab = set()
        for i, text in docs.items():
            words = text.lower().split()
            self.vocab.update(words)
            for w in words:
                self.index[w].add(i)
    def dist(self, a, b):
        dp = [[i+j if i*j==0 else 0 for j in range(len(b)+1)]
              for i in range(len(a)+1)]
        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                dp[i][j] = min(
                    dp[i-1][j] + 1,
                    dp[i][j-1] + 1,
                    dp[i-1][j-1] + (a[i-1] != b[j-1])
                )
        return dp[-1][-1]
    def correct(self, w):
        return min(self.vocab, key=lambda v: self.dist(w, v))
    def search(self, q):
        words = [self.correct(w) for w in q.lower().split()]
        print("Corrected Query:", " ".join(words))
        sets = [self.index[w] for w in words if w in self.index]
        return set.intersection(*sets) if sets else set()
docs = {
    1: "web content extraction involves retrieving structured data",
    2: "search engines use document indexing for efficient retrieval",
    3: "document retrieval is important in web mining applications",
    4: "indexing helps in retrieving relevant documents"
}
ir = IR(docs)
queries = ["retrievel", "documnt indexing", "web minng", "strctured data"]
print("\n=== Results ===")
for q in queries:
    res = ir.search(q)
    print(f"Query: '{q}' -> {sorted(res) if res else 'No match'}")