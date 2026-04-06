def pagerank(graph, d=0.85, iters=100, tol=1e-6):
    n = len(graph)
    pr = {p: 1/n for p in graph}
    for _ in range(iters):
        new = {}
        for page in graph:
            incoming = [p for p in graph if page in graph[p]]
            s = sum(pr[p] / len(graph[p]) for p in incoming)
            new[page] = (1 - d)/n + d * s
        if all(abs(new[p] - pr[p]) < tol for p in pr):  # convergence check
            pr = new
            break
        pr = new
    return pr

web = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

scores = pagerank(web)
print("\n=== PageRank Scores ===")
for page, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"Page {page}: {round(score, 6)}")