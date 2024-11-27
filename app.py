import streamlit as st
import numpy as np
import pandas as pd

def calculate_scores(data):
    savings_score = min(data['savings_to_income'] * 200, 100)
    expenses_score = max(100 - (data['expenses_to_income'] * 200), 0)
    loan_score = max(100 - (data['loan_to_income'] * 200), 0)
    credit_card_score = max(100 - (data['credit_card_to_total_spending'] * 200), 0)
    financial_goals_score = min(data['financial_goals_met'], 100)

    return {
        "Savings_Score": savings_score,
        "Expenses_Score": expenses_score,
        "Loan_Score": loan_score,
        "Credit_Card_Score": credit_card_score,
        "Financial_Goals_Score": financial_goals_score,
    }

def calculate_final_score(scores, weights):
    final_score = (
        scores['Savings_Score'] * weights['Savings_Score'] +
        scores['Expenses_Score'] * weights['Expenses_Score'] +
        scores['Loan_Score'] * weights['Loan_Score'] +
        scores['Credit_Card_Score'] * weights['Credit_Card_Score'] +
        scores['Financial_Goals_Score'] * weights['Financial_Goals_Score']
    )
    return round(final_score, 2)


def generate_recommendations(scores):
    recommendations = []
    if scores["Savings_Score"] < 50:
        recommendations.append("Increase savings by at least 10% to improve your score.")
    if scores["Expenses_Score"] < 50:
        recommendations.append("Reduce discretionary spending by 10% to boost your score.")
    if scores["Loan_Score"] < 50:
        recommendations.append("Reduce loan payments or restructure to lower your financial burden.")
    if scores["Credit_Card_Score"] < 50:
        recommendations.append("Minimize credit card spending to enhance your score.")
    if scores["Financial_Goals_Score"] < 50:
        recommendations.append("Focus on meeting more financial goals to improve your overall health.")
    
    return recommendations


st.title("Family Financial Scoring App")

st.sidebar.header("Input Family Financial Data")
savings_to_income = st.sidebar.slider("Savings to Income Ratio", 0.0, 1.0, 0.3)
expenses_to_income = st.sidebar.slider("Expenses to Income Ratio", 0.0, 1.0, 0.5)
loan_to_income = st.sidebar.slider("Loan to Income Ratio", 0.0, 1.0, 0.2)
credit_card_to_total_spending = st.sidebar.slider("Credit Card Spending to Total Spending Ratio", 0.0, 1.0, 0.1)
financial_goals_met = st.sidebar.slider("Financial Goals Met (%)", 0, 100, 80)


weights = {
    'Savings_Score': 0.25,
    'Expenses_Score': 0.20,
    'Loan_Score': 0.15,
    'Credit_Card_Score': 0.15,
    'Financial_Goals_Score': 0.10,
}

input_data = {
    'savings_to_income': savings_to_income,
    'expenses_to_income': expenses_to_income,
    'loan_to_income': loan_to_income,
    'credit_card_to_total_spending': credit_card_to_total_spending,
    'financial_goals_met': financial_goals_met
}

scores = calculate_scores(input_data)
final_score = calculate_final_score(scores, weights)
recommendations = generate_recommendations(scores)


st.subheader("Financial Scores")
st.json(scores)


st.subheader(f"Final Financial Health Score: {final_score}")


st.subheader("Recommendations")
for rec in recommendations:
    st.write(f"- {rec}")

st.subheader("Visualization of Scores")
scores_df = pd.DataFrame(scores, index=[0]).melt(var_name="Score Type", value_name="Value")
st.bar_chart(data=scores_df, x="Score Type", y="Value", use_container_width=True)
