from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
documents = [
    "I love this product, it is amazing",
    "This is the worst experience ever",
    "Absolutely fantastic service",
    "I am very disappointed with this item",
    "Great quality and fast delivery",
    "Terrible product, not recommended"
]
labels = [1, 0, 1, 0, 1, 0]
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, zero_division=0))
sentence = ["The product is excellent and I love it"]
prediction = model.predict(vectorizer.transform(sentence))
print("Sentiment:", "Positive" if prediction[0] == 1 else "Negative")