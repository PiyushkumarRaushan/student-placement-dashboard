import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
df = pd.read_csv("students.csv")

# Convert Yes/No to 1/0
df["Placed"] = df["Placed"].map({
    "Yes": 1,
    "No": 0
})

# Features
X = df[
    [
        "CGPA",
        "Internships",
        "Projects",
        "Aptitude"
    ]
]

# Target
y = df["Placed"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model
model = LogisticRegression()

# Train
model.fit(
    X_train,
    y_train
)

# Prediction
prediction = model.predict(
    [[8.5, 2, 3, 85]]
)

print(
    "Prediction:",
    "Placed" if prediction[0] == 1 else "Not Placed"
)


y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print(
    "Accuracy:",
    round(accuracy * 100, 2),
    "%"
)

joblib.dump(
    model,
    "placement_model.pkl"
)

print("Model Saved")