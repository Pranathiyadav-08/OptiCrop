import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("data/processed_crop.csv")

# Encode season
le = LabelEncoder()
df['season'] = le.fit_transform(df['season'])

# Features & label
X = df[['N','P','K','temperature','humidity','ph','rainfall','season']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Accuracy
print("Model Accuracy:", model.score(X_test, y_test))

# Prediction example
sample = [[90,42,43,20.8,82,6.5,202,1]]
print("Predicted crop:", model.predict(sample))