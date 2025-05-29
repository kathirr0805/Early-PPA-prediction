# train_models.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib
import os

# Load your dataset (replace with your actual CSV)
df = pd.read_csv("dataset.csv")

# Assume 'RTL' is the Verilog text, and target columns are area, delay, static_power
X_raw = df['RTL']
y_area = df['area']
y_delay = df['delay']
y_power = df['static_power']

# TF-IDF Feature Extraction
vectorizer = TfidfVectorizer(max_features=1000)
X_vec = vectorizer.fit_transform(X_raw)

# Train/Test split
X_train, X_test, y_area_train, y_area_test = train_test_split(X_vec, y_area, test_size=0.2, random_state=42)
_, _, y_delay_train, _ = train_test_split(X_vec, y_delay, test_size=0.2, random_state=42)
_, _, y_power_train, _ = train_test_split(X_vec, y_power, test_size=0.2, random_state=42)

# Train Models
area_model = RandomForestRegressor()
area_model.fit(X_train, y_area_train)

delay_model = RandomForestRegressor()
delay_model.fit(X_train, y_delay_train)

power_model = RandomForestRegressor()
power_model.fit(X_train, y_power_train)

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(area_model, "models/area_model.pkl")
joblib.dump(delay_model, "models/delay_model.pkl")
joblib.dump(power_model, "models/power_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Models trained and saved in 'models/' directory.")
