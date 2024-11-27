from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


app = FastAPI()


class FamilyData(BaseModel):
    savings_to_income: float
    expenses_to_income: float
    loan_to_income: float
    credit_card_to_total_spending: float
    financial_goals_met: float


weights = {
    'Savings_Score': 0.25,
    'Expenses_Score': 0.20,
    'Loan_Score': 0.15,
    'Credit_Card_Score': 0.15,
    'Financial_Goals_Score': 0.10,
}


def calculate_scores(data):
    savings_score = (data.savings_to_income * 200).clip(upper=100)
    expenses_score = (100 - (data.expenses_to_income * 200)).clip(lower=0)
    loan_score = (100 - (data.loan_to_income * 200)).clip(lower=0)
    credit_card_score = (100 - (data.credit_card_to_total_spending * 200)).clip(lower=0)
    financial_goals_score = data.financial_goals_met.clip(lower=0, upper=100)

    return {
        "Savings_Score": savings_score,
        "Expenses_Score": expenses_score,
        "Loan_Score": loan_score,
        "Credit_Card_Score": credit_card_score,
        "Financial_Goals_Score": financial_goals_score,
    }


def calculate_final_score(scores):
    final_score = (
        scores['Savings_Score'] * weights['Savings_Score'] +
        scores['Expenses_Score'] * weights['Expenses_Score'] +
        scores['Loan_Score'] * weights['Loan_Score'] +
        scores['Credit_Card_Score'] * weights['Credit_Card_Score'] +
        scores['Financial_Goals_Score'] * weights['Financial_Goals_Score']
    )
    return round(final_score, 2)


def generate_insights(scores):
    insights = []
    if scores["Savings_Score"] < 50:
        insights.append("Savings are below recommended levels, which affects your score.")
    if scores["Expenses_Score"] < 50:
        insights.append("High expenses reduce your financial health score.")
    if scores["Loan_Score"] < 50:
        insights.append("Loan payments are too high relative to income.")
    if scores["Credit_Card_Score"] < 50:
        insights.append("High credit card spending negatively impacts your score.")
    if scores["Financial_Goals_Score"] < 50:
        insights.append("Meeting more financial goals can improve your score.")
    
    return insights


@app.post("/score")
def calculate_financial_health(data: FamilyData):
    scores = calculate_scores(data)
    final_score = calculate_final_score(scores)
    insights = generate_insights(scores)
    
    return {
        "Final_Score": final_score,
        "Scores": scores,
        "Insights": insights
    }
def read_root():
    return {"message": "Hello, World!"}
@app.get("/")
def read_root():
    return {"message": "Welcome to the Financial Scoring API! Use /score to calculate financial health."}

