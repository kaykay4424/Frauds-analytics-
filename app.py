import streamlit as st
import pandas as pd
import numpy as np
from groq import Groq
import pickle


# ---- CONFIG ----
st.set_page_config(page_title="K's UPI Fraud Intelligence", page_icon="🔍", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0a;
        color: #00ff41;
        font-family: 'Courier New', monospace;
    }
    .kpi-card {
        background-color: #0d1a0d;
        border: 1px solid #00ff41;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        margin: 10px;
    }
    .kpi-value {
        font-size: 36px;
        font-weight: bold;
        color: #00ff41;
        text-shadow: 0 0 10px #00ff41, 0 0 20px #00ff41;
    }
    .kpi-label {
        font-size: 12px;
        color: #7dff7d;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    .stTextInput > div > div > input {
        background-color: #0d1a0d;
        color: #00ff41;
        border: 1px solid #00ff41;
        border-radius: 4px;
        font-family: 'Courier New', monospace;
    }
    .answer-box {
        background-color: #0d1a0d;
        border: 1px solid #00ff41;
        border-left: 4px solid #00ff41;
        border-radius: 4px;
        padding: 20px;
        margin-top: 20px;
        color: #00ff41;
        font-family: 'Courier New', monospace;
        animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .main-header h1::after {
        content: '_';
        animation: blink 1s infinite;
    }
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    .sample-question {
        background-color: #0d1a0d;
        border: 1px solid #1a4d1a;
        border-radius: 4px;
        padding: 8px 15px;
        margin: 5px;
        color: #7dff7d;
        font-size: 13px;
        display: inline-block;
    }
    hr { border-color: #1a4d1a; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
#__________________________
# ---- GROQ CLIENT ----
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---- FRAUD SUMMARY (from our analysis) ----
fraud_summary = """
Dataset analyzed: 284,807 UPI transactions
Total fraud cases: 492 (0.17%)
Model: XGBoost with 89% fraud recall
Test results: 87 out of 98 fraud cases correctly flagged

Key insights:
- 50% of fraud transactions are under 9.25 rupees
- Fraud peaks at 9 PM (hour 21)
- Top fraud indicators: V14 (22% importance), V10 (11%), V4 (11%)
- Normal transactions follow day/night cycle, fraud does not
- False alarm rate: only 18 normal transactions wrongly flagged
- Average fraud amount: 122 rupees vs 88 rupees for normal
"""

# ---- AI ANSWER FUNCTION ----
def answer_question(question):
    prompt = f"""
    You are a fraud analytics expert helping a business team understand their fraud detection results.
    Answer the following question in simple, non-technical business language in 3-4 sentences.
    Be specific and use the data provided.
    
    Fraud Detection Analysis:
    {fraud_summary}
    
    Business Question: {question}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---- UI ----
st.divider()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Transactions", "284,807")
col2.metric("Fraud Cases", "492", "0.17%")
col3.metric("Fraud Recall", "89%", "XGBoost")
col4.metric("Avg Fraud Amount", "₹122")

st.divider()

# Chat
st.subheader("💬 Ask a Business Question")
question = st.text_input("Type your question:", placeholder="e.g. When should we increase fraud monitoring?")

if question:
    with st.spinner("Analyzing..."):
        answer = answer_question(question)
    st.success("**AI Analysis:**")
    st.write(answer)
