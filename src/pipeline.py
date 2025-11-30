# src/pipeline.py

import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# 1. Load dataset
DATA_PATH = "./assets/opinion_dataset.csv"
df = pd.read_csv(DATA_PATH)

# 2. Basic text cleaning function
def clean_text(text):
    text = text.lower()  # lowercase
    text = text.translate(str.maketrans("", "", string.punctuation))  # remove punctuation
    return text

df['clean_text'] = df['text'].apply(clean_text)

# 3. Split into training and test sets
X = df['clean_text']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Create pipeline: TF-IDF + Logistic Regression
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=1000)),
    ("clf", LogisticRegression(multi_class="ovr", max_iter=500))
])

# 5. Train the model
pipeline.fit(X_train, y_train)

# 6. Evaluate on test set
y_pred = pipeline.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 7. Save the trained pipeline
MODEL_PATH = "./assets/model.joblib"
joblib.dump(pipeline, MODEL_PATH)
print(f"Model saved to {MODEL_PATH}")
