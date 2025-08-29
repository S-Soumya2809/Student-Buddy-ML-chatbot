import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import joblib
import os

df = pd.read_csv("leetcode_dataset.csv")
df = df.dropna(subset=['title', 'description'])
df['text'] = df['title'] + " " + df['description']

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])

knn = NearestNeighbors(n_neighbors=1, metric='cosine')
knn.fit(X)

os.makedirs("model", exist_ok=True)
joblib.dump(knn, "model/knn_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")
df.to_csv("model/problems.csv", index=False)

print("✅ Model trained and saved.")