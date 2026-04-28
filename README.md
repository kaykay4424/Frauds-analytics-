#  Groq LLaMa 3.1-Integrated UPI Fraud Detection System and Analysis
---
## LIVE APP: https://7p8lx6ol5fet62k4xpmqfk.streamlit.app/#upi-fraud-intelligence-system
---
## Overview
This end-to-end live Product fills the communication bridge between the messy technical data & nontechnical person, Where you can simply ask your business queries and get answers based on the accurate insights by Groq LLaMA 3.1 LLM.
---

## Dashboard Preview
---
<img width="1305" height="740" alt="Dashboard" src="https://github.com/user-attachments/assets/8094e513-5484-4ca7-849d-2ef7acc669a3" />

## Key Results

| Model | Fraud Recall | Precision | F1 Score |
|-------|-------------|-----------|----------|
| Random Forest | 81% | 81% | 81% |
| **XGBoost** | **89%** | **73%** | **80%** |

**XGBoost chosen as final model — catches 89% of all fraud cases**

---

## Key Findings from EDA
- **Fraudsters deliberately keep transaction amounts small** — 50% of fraud transactions are under ₹9.25, deliberately staying below detection thresholds
- **Fraud peaks at 9 PM** — highest fraud activity at hour 21, when monitoring may be lower but users are still active
- **Fraud has no consistent time pattern** — unlike normal transactions which follow human sleep/wake cycles, fraud occurs randomly suggesting automated bots or geographically dispersed actors
- **V14 is the strongest fraud signal** — Feature importance analysis identified V14 (22%), V10 (11%), and V4 (11%) as primary fraud indicators
- **Amount alone cannot detect fraud** — correlation analysis showed Amount has very weak relationship with fraud class, confirming sophisticated fraud avoidance strategies

---

## Tech Stack
- **Python** — Pandas, NumPy, Scikit-learn, XGBoost, Imbalanced-learn
- **Machine Learning** — Random Forest, XGBoost, SMOTE
- **GenAI** — Groq LLaMA 3.1 for business intelligence query answering
- **Frontend** — Streamlit with Bloomberg-style terminal UI
- **Visualization** — Seaborn, Matplotlib, Power BI Dashboard
- **Data** — 284,807 real transactions, 492 confirmed fraud cases
---

## Pipeline
```
Raw Data → EDA → Feature Engineering → SMOTE Balancing → Model Training → Evaluation → GenAI Explanation → Streamlit app → Dashboard
```

**Step 1 — Exploratory Data Analysis**
- Transaction amount distribution by class
- Time-based fraud pattern analysis
- Feature correlation heatmap
- Class imbalance visualization

**Step 2 — Data Preparation**
- StandardScaler on Amount and Time features
- Train/Test split (80/20) with stratification
- SMOTE applied on training data only to handle 0.17% fraud minority class

**Step 3 — Model Building**
- Random Forest (100 estimators)
- XGBoost classifier
- Evaluation using Precision, Recall, F1 — prioritizing Recall

**Step 4 — Feature Importance**
- Top fraud signals: V14, V10, V4, V17, V12
- V14 alone accounts for 22% of model decisions

**Step 5 — GenAI Business Intelligence Layer**
- XGBoost flags suspicious transactions with probability score
- Groq LLaMA 3.1 answers business questions in plain English
- No technical knowledge required — just ask naturally
- Bloomberg-style terminal UI for professional presentation

**Step 6 — Deployment**
- Live on Streamlit Cloud
- Accessible via public link
- Secure API key management via Streamlit secrets

---

## Business Impact
- Model detects **89% of fraudulent transactions**
- Out of 98 fraud cases in test data — **87 correctly flagged**
- Only **11 fraud cases missed**
- At average fraud value of ₹122 — model potentially prevents **₹10,614 in losses per test batch**
- Fraud peaks at **9 PM** — actionable insight for enhanced monitoring windows
- False alarm rate kept low — only 18 normal transactions incorrectly flagged
---

## Future Improvements
- Upload your own csv feature
- SHAP values for model explainability
- Neural network comparison
- Live UPI transaction simulation
- Anomaly detection using Isolation Forest

---

## Made by:

**Krish Kamboj**
- LinkedIn: [linkedin.com/in/krish-kamboj-618845224](https://www.linkedin.com/in/krish-kamboj-618845224/)
- GitHub: [github.com/kaykay4424](https://github.com/kaykay4424/kaykay4424)
- Email: Krishkamboj09876@gmail.com

---

## Dataset

UCI Machine Learning Repository — Credit Card Fraud Detection Dataset
Provided by Worldline and the Machine Learning Group of ULB

---
