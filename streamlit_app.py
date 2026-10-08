import pandas as pd
import streamlit as st
from pathlib import Path
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")
st.title("Customer Churn Prediction Dashboard")
st.caption("Train a churn model and view performance statistics.")


def get_default_csv_path():
    csv_files = sorted(Path(".").glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError("No CSV files found in the project folder.")
    return str(csv_files[0])


def load_data(uploaded_file):
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return pd.read_csv(get_default_csv_path())


def clean_data(df):
    df = df.drop_duplicates()

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    cat_cols = df.columns.difference(num_cols)
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    if "Churn" not in df.columns:
        raise ValueError("Dataset must include a 'Churn' column.")

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    if df["Churn"].isna().any():
        raise ValueError("'Churn' values must be 'Yes' or 'No'.")

    return df


st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload churn CSV", type=["csv"])
test_size = st.sidebar.slider("Test size", min_value=0.1, max_value=0.4, value=0.2, step=0.05)
random_state = st.sidebar.number_input("Random state", min_value=0, max_value=999, value=42)

try:
    source_name = uploaded_file.name if uploaded_file is not None else get_default_csv_path()
    df = load_data(uploaded_file)
    df = clean_data(df)
except Exception as exc:
    st.error(f"Could not load dataset: {exc}")
    st.stop()

st.sidebar.caption(f"Data source: {source_name}")

st.subheader("Dataset Preview")
st.dataframe(df.head(), width="stretch")

churn_counts = df["Churn"].map({1: "Yes", 0: "No"}).value_counts()
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("**Rows / Columns**")
    st.write(f"{df.shape[0]} rows, {df.shape[1]} columns")
with col_b:
    st.markdown("**Churn Distribution**")
    st.bar_chart(churn_counts)

X = df.drop("Churn", axis=1)
y = df["Churn"]

num_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
cat_cols = X.columns.difference(num_cols).tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ]
)

model = RandomForestClassifier(n_estimators=200, max_depth=None, random_state=int(random_state))

clf = Pipeline(steps=[("preprocess", preprocessor), ("model", model)])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=test_size,
    random_state=int(random_state),
    stratify=y,
)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)

st.subheader("Model Statistics")
metric_1, metric_2, metric_3 = st.columns(3)
metric_1.metric("Accuracy", f"{accuracy:.3f}")
metric_2.metric("Precision", f"{precision:.3f}")
metric_3.metric("Recall", f"{recall:.3f}")

st.markdown("**Confusion Matrix**")
cm = confusion_matrix(y_test, y_pred)
cm_df = pd.DataFrame(cm, index=["Actual No", "Actual Yes"], columns=["Pred No", "Pred Yes"])
st.dataframe(cm_df, width="stretch")

st.markdown("**Classification Report**")
report = classification_report(y_test, y_pred, output_dict=True, zero_division=0)
report_df = pd.DataFrame(report).transpose()
st.dataframe(report_df, width="stretch")

st.markdown("**Sample Prediction (first row)**")
sample = X.iloc[[0]]
sample_pred = clf.predict(sample)[0]
st.write("Prediction:", "Yes" if sample_pred == 1 else "No")
