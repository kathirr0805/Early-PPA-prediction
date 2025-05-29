import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import joblib

vectorizer = joblib.load("models/vectorizer.pkl")

def extract_features_from_verilog(code):
    features = vectorizer.transform([code]).toarray()
    return features
