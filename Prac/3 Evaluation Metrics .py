relevant_documents = {1, 2, 3, 5, 7}
retrieved_documents = {1, 2, 4, 5, 6}

tp = len(relevant_documents & retrieved_documents)
fp = len(retrieved_documents - relevant_documents)
fn = len(relevant_documents - retrieved_documents)

precision = tp / (tp + fp) if tp + fp != 0 else 0
recall = tp / (tp + fn) if tp + fn != 0 else 0
f1_score = 2 * precision * recall / (precision + recall) if precision + recall != 0 else 0

print("Evaluation Metrics for Information Retrieval")
print(f"True Positives (TP): {tp}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1_score:.4f}")