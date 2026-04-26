import streamlit as st
from groq import Groq

.reach-out {
    margin-left: auto;
    position: relative;
    cursor: pointer;
}

.reach-out-btn {
    color: #00a8e8;
    
    cursor: pointer;
    font-weight: 600;
}

.reach-out-dropdown {
    display: none;
    position: absolute;
    right: 0;

    background-color: #1a1a1a;
    border: 1px solid #00a8e8;
    padding: 10px 15px;
    z-index: 9999;
    min-width: 200px;
}

.reach-out:hover .reach-out-dropdown {
    display: block;
}

.reach-out-dropdown a {
    display: block;
    color: #e0e0e0;
    text-decoration: none;
    padding: 5px 0;
    font-size: 11px;
    letter-spacing: 1px;
}

.reach-out-dropdown a:hover {
    color: #00a8e8;
}
    
st.set_page_config(page_title="K's Fraud Intelligence Terminal", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300;400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

* { font-family: 'IBM Plex Sans', sans-serif; }

.stApp {
    background-color: #0f0f0f;
    color: #e0e0e0;
}

/* Top ticker bar */
.ticker-bar {
    background-color: #1a1a1a;
    border-bottom: 1px solid #00a8e8;
    padding: 6px 20px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #00a8e8;
    letter-spacing: 1px;
    display: flex;
    gap: 30px;
    margin-bottom: 20px;
}

.ticker-item {
    display: inline;
}

.ticker-up { color: #00d4aa; }
.ticker-down { color: #ff4444; }

/* Header */
.terminal-header {
    background-color: #1a1a1a;
    border-left: 4px solid #00a8e8;
    padding: 15px 25px;
    margin-bottom: 25px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* KPI Cards */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 25px;
}

.kpi-card {
    background-color: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-top: 2px solid #00a8e8;
    padding: 18px;
}

.kpi-label {
    font-size: 10px;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-family: 'IBM Plex Mono', monospace;
    margin-bottom: 8px;
}

.kpi-value {
    font-size: 28px;
    font-weight: 600;
    color: #ffffff;
    font-family: 'IBM Plex Mono', monospace;
}

.kpi-sub {
    font-size: 11px;
    color: #00d4aa;
    margin-top: 4px;
    font-family: 'IBM Plex Mono', monospace;
}

/* Section headers */
.section-header {
    background-color: #1a1a1a;
    border-left: 3px solid #00a8e8;
    padding: 8px 15px;
    font-size: 11px;
    font-family: 'IBM Plex Mono', monospace;
    color: #00a8e8;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 15px;
}

/* Query chips */
.query-chip {
    display: inline-block;
    background-color: #1a1a1a;
    border: 1px solid #2a2a2a;
    padding: 5px 12px;
    margin: 4px;
    font-size: 11px;
    color: #888;
    font-family: 'IBM Plex Mono', monospace;
    cursor: pointer;
}

.query-chip:hover { border-color: #00a8e8; color: #00a8e8; }

/* Input */
.stTextInput > div > div > input {
    background-color: #1a1a1a !important;
    color: #e0e0e0 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 0px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 13px !important;
    padding: 12px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00a8e8 !important;
}

/* Answer panel */
.answer-panel {
    background-color: #1a1a1a;
    border: 1px solid #2a2a2a;
    border-left: 3px solid #00d4aa;
    padding: 20px;
    margin-top: 15px;
    font-family: 'IBM Plex Sans', sans-serif;
    font-size: 14px;
    color: #e0e0e0;
    line-height: 1.7;
    animation: slideIn 0.3s ease;
}

.answer-query {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #00a8e8;
    letter-spacing: 1px;
    margin-bottom: 12px;
    text-transform: uppercase;
}

@keyframes slideIn {
    from { opacity: 0; transform: translateY(-5px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Divider */
.divider {
    border: none;
    border-top: 1px solid #2a2a2a;
    margin: 20px 0;
}

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---- GROQ CLIENT ----
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---- FRAUD SUMMARY ----
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

# ---- AI FUNCTION ----
def answer_question(question):
    prompt = f"""
    You are a senior fraud analytics expert at a top financial institution.
    Answer the following business question based on the fraud detection analysis.
    Be concise, data-driven, and use business language. 3-4 sentences max.
    
    Analysis Data:
    {fraud_summary}
    
    Question: {question}
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ---- TICKER BAR ----
st.markdown("""
<div class="ticker-bar">
    <span>FRAUD INTELLIGENCE TERMINAL v1.0</span>
    <span>|</span>
    <span class="ticker-up">MODEL: XGBOOST ▲ 89% RECALL</span>
    <span>|</span>
    <span>TRANSACTIONS: 284,807</span>
    <span>|</span>
    <span class="ticker-down">FRAUD RATE: 0.17%</span>
    <span>|</span>
    <span>POWERED BY GROQ LLM</span>
<div class="reach-out">
    <span class="reach-out-btn">[ REACH OUT ▾ ]</span>
    <div class="reach-out-dropdown">
        <a href="mailto:Krishkamboj09876@gmail.com">✉ Krishkamboj09876@gmail.com</a>
        <a href="https://www.linkedin.com/in/krish-kamboj-618845224/" target="_blank">in LinkedIn Profile</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<div class="terminal-header">
    <div>
        <div style="font-size: 11px; color: #00a8e8; letter-spacing: 3px; font-family: IBM Plex Mono; margin-bottom: 5px;">
            KRISH KAMBOJ · FRAUD ANALYTICS
        </div>
        <div style="font-size: 22px; font-weight: 600; color: #ffffff; letter-spacing: 1px;">
            K's Fraud Insights Terminal
        </div>
    </div>
    <div style="text-align: right; font-family: IBM Plex Mono; font-size: 11px; color: #888;">
        <div style="color: #00d4aa; font-size: 13px; font-weight: 600;">● LIVE</div>
        <div>XGBOOST + LLM</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- KPI CARDS ----
st.markdown("""
<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-label">Total Transactions</div>
        <div class="kpi-value">284,807</div>
        <div class="kpi-sub">▲ Dataset Analyzed</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Fraud Detected</div>
        <div class="kpi-value">492</div>
        <div class="kpi-sub" style="color: #ff4444;">▲ 0.17% Rate</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Model Recall</div>
        <div class="kpi-value">89%</div>
        <div class="kpi-sub">▲ XGBoost Model</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Avg Fraud Amount</div>
        <div class="kpi-value">₹122</div>
        <div class="kpi-sub" style="color: #ff4444;">▼ vs ₹88 Normal</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---- QUERY SECTION ----
st.markdown('<div class="section-header">▶ INTELLIGENCE QUERY INTERFACE</div>', unsafe_allow_html=True)

st.markdown("""
<div style="margin-bottom: 12px;">
    <span class="query-chip">When to increase monitoring?</span>
    <span class="query-chip">Most risky amount range?</span>
    <span class="query-chip">Model accuracy breakdown?</span>
    <span class="query-chip">Block small transactions?</span>
    <span class="query-chip">Peak fraud hours?</span>
</div>
""", unsafe_allow_html=True)

# ---- CHAT ----
if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input("", placeholder="Enter intelligence query...")

if question:
    with st.spinner("Processing..."):
        answer = answer_question(question)
    st.session_state.history.append((question, answer))

for q, a in reversed(st.session_state.history):
    st.markdown(f"""
    <div class="answer-panel">
        <div class="answer-query">▶ {q}</div>
        <div>{a}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="font-family: IBM Plex Mono; font-size: 10px; color: #444; text-align: center; padding: 10px;">
    FRAUD INTELLIGENCE TERMINAL · BUILT BY KRISH KAMBOJ · XGBOOST + GROQ LLM
</div>
""", unsafe_allow_html=True)
