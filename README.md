# 📉 Customer Churn Prediction

> Predicting customer churn using Random Forest classification, MySQL analysis, Tableau dashboards, and an interactive Streamlit web app.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![Tableau](https://img.shields.io/badge/Tableau-Visualization-lightblue?logo=tableau)

---

## 🎯 Problem Statement

Customer churn is one of the most costly problems for subscription-based businesses. This project builds an end-to-end ML pipeline to identify **which customers are likely to leave**, enabling proactive retention strategies.

---

## ✅ Model Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | **75%** |
| **Precision** | **0.69** |
| Algorithm | Random Forest |

---

## 🖥️ Dashboard Preview

> *Run `streamlit run streamlit_app.py` to launch the interactive dashboard locally.*

*(Screenshot coming soon)*

---

## 🗂️ Project Structure

```
├── customer_churn.py                 # ML pipeline: data cleaning, training, evaluation
├── streamlit_app.py                  # Interactive Streamlit dashboard
├── customer_churn_prediction.csv     # Dataset
├── requirements.txt                  # Dependencies
├── MySQL/
│   ├── schema.sql                    # Database structure
│   ├── queries.sql                   # Analytical SQL queries
│   └── data_import.sql               # Data import scripts
└── Tableau/
    ├── churn_analysis.twbx           # Churn breakdown by segment
    └── customer_insights.twbx        # Customer behavior dashboard
```

---

## ⚙️ How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/pranav-codes55/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python customer_churn.py

# 4. Launch the dashboard
streamlit run streamlit_app.py
```
The app opens at `http://localhost:8501`

---

## 🔧 Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.x |
| ML | Scikit-learn (Random Forest) |
| Data | Pandas, NumPy |
| Dashboard | Streamlit |
| Database | MySQL |
| Visualization | Tableau |

---

## 📊 What the Pipeline Does

```
CSV Data → MySQL (storage + SQL analysis) → Python ML Model → Predictions
                        ↓
               Tableau Dashboards ← SQL Queries
                        ↓
               Streamlit Dashboard ← Model Output
```

---

## 👤 Author

**Pranav R P** — [LinkedIn](https://www.linkedin.com/in/pranav-rp-a89635314/) · [GitHub](https://github.com/pranav-codes55)
