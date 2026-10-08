# --------------------------------------------------------
# 1. Import libraries
# --------------------------------------------------------
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)
from sklearn.ensemble import RandomForestClassifier

# --------------------------------------------------------
# 2. Load dataset
# --------------------------------------------------------
csv_files = sorted(Path(".").glob("*.csv"))
if not csv_files:
    raise FileNotFoundError("No CSV files found in project folder.")

df = pd.read_csv(csv_files[0])
print(f"Using dataset: {csv_files[0]}")
print(df.head())
print(df.info())

# --------------------------------------------------------
# 3. Clean data
# --------------------------------------------------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing numerical values with median
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill missing categorical values with mode
cat_cols = df.columns.difference(num_cols)
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

# --------------------------------------------------------
# 4. Convert Yes/No to numerical 1/0 for target variable
# --------------------------------------------------------
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# --------------------------------------------------------
# 5. Separate features and target
# --------------------------------------------------------
X = df.drop("Churn", axis=1)
y = df["Churn"]

# Identify numerical + categorical columns
num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = X.columns.difference(num_cols).tolist()

# --------------------------------------------------------
# 6. Preprocessing (Scaling + Encoding)
# --------------------------------------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ]
)

# --------------------------------------------------------
# 7. Choose model
# --------------------------------------------------------
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    random_state=42
)

# --------------------------------------------------------
# 8. Build pipeline
# --------------------------------------------------------
clf = Pipeline(steps=[
    ("preprocess", preprocessor),
    ("model", model)
])

# --------------------------------------------------------
# 9. Train-Test Split
# --------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# --------------------------------------------------------
# 10. Train the model
# --------------------------------------------------------
clf.fit(X_train, y_train)

# --------------------------------------------------------
# 11. Predictions
# --------------------------------------------------------
y_pred = clf.predict(X_test)

# --------------------------------------------------------
# 12. Evaluation
# --------------------------------------------------------
print("Accuracy: ", accuracy_score(y_test, y_pred))
print("Precision: ", precision_score(y_test, y_pred))
print("Recall: ", recall_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# --------------------------------------------------------
# 13. Predict for a new customer (example)
# --------------------------------------------------------
sample = X.iloc[[0]]        # use any row as sample
print("\nPrediction for sample:", clf.predict(sample))