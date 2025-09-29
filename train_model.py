# train_model.py
import random
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# DNA dizisi üretici
def generate_dna_sequence(length=50):
    return "".join(random.choice("ATCG") for _ in range(length))

# Sağlıklı ve mutant diziler
healthy_sequences = [generate_dna_sequence() for _ in range(200)]
mutant_sequences = [generate_dna_sequence().replace("A", "G", 5) for _ in range(200)]

X = healthy_sequences + mutant_sequences
y = [0]*200 + [1]*200  # 0 = Healthy, 1 = Mutant

# DNA dizilerini sayısal vektörlere dönüştür
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 2))
X_vectorized = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Model eğitimi
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Doğruluk raporu
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# Model ve vectorizer kaydet
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model ve vectorizer kaydedildi.")
