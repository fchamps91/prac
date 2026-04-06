from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
categories = ['alt.atheism', 'rec.motorcycles', 'comp.graphics', 'sci.med']
data = fetch_20newsgroups(subset='all', categories=categories,
                          remove=('headers', 'footers', 'quotes'))
X = TfidfVectorizer(stop_words='english').fit_transform(data.data)
y = data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
nb = MultinomialNB()
nb.fit(X_train, y_train)
pred_nb = nb.predict(X_test)
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)
pred_svm = svm.predict(X_test)
print("\n=== Naive Bayes ===")
print("Accuracy:", round(accuracy_score(y_test, pred_nb), 4))
print(classification_report(y_test, pred_nb, target_names=categories))
print("\n=== SVM ===")
print("Accuracy:", round(accuracy_score(y_test, pred_svm), 4))
print(classification_report(y_test, pred_svm, target_names=categories))