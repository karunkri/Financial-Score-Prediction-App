# Financial Score Prediction App

This project implements a web-based application using **Streamlit** to allow users to interact with a financial scoring model. The app takes user inputs, calculates financial scores, and provides actionable recommendations for improvement.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Model Logic](#model-logic)
4. [Features](#features)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

The Financial Score Prediction App computes a financial score based on user input related to income, savings, expenses, and debt. It provides:
- Insights into the user’s financial health.
- Personalized recommendations to improve their score.

This project is intended for educational purposes or as a starting point for building more advanced financial modeling applications.

---

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- The following Python libraries:
  - `streamlit`
  - `pandas`
  - `numpy`

### Installation

1. **Clone the Repository**  
   ```
   git clone https://github.com//financial-score-app](https://github.com/karunkri/Financial-Score-Prediction-App.git
   cd financial-score-app
   ```

2. **Set Up a Virtual Environment**  
   ```
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   Use the following command to start the Streamlit app:
   ```
   streamlit run app.py
   ```

5. **Access the App**  
   Open your web browser and navigate to the URL provided by Streamlit (e.g., `http://localhost:8501`).

6. **Start the FastAPI server**
 Use the following command to start the FastAPI server:
```
uvicorn main:app --reload
```

---

## Model Logic

### Input Data
The model takes the following inputs:
- **Income**: User’s monthly income.
- **Savings**: Total savings available.
- **Expenses**: Monthly expenses.
- **Debt**: Current outstanding debt.

### Score Calculation
1. **Savings-to-Income Ratio**  
   A higher ratio indicates better financial health.
   \[
   \text{savings\_score} = \min\left(\frac{\text{savings}}{\text{income}} \times 200, 100\right)
   \]

2. **Debt-to-Income Ratio**  
   Lower ratios yield better scores.
   \[
   \text{debt\_score} = \max\left(100 - \frac{\text{debt}}{\text{income}} \times 100, 0\right)
   \]

3. **Expense-to-Income Ratio**  
   Low expenses compared to income improve the score.
   \[
   \text{expense\_score} = \max\left(100 - \frac{\text{expenses}}{\text{income}} \times 100, 0\right)
   \]

4. **Final Score**  
   The final score is a weighted average of the individual components:
   \[
   \text{final\_score} = 0.4 \times \text{savings\_score} + 0.3 \times \text{debt\_score} + 0.3 \times \text{expense\_score}
   \]

### Recommendations
Based on the computed scores, the app provides actionable suggestions, such as:
- Reducing discretionary spending by a certain percentage.
- Allocating more income to savings.
- Prioritizing debt repayments.

---

## Features

- User-friendly interface for inputting financial data.
- Real-time score computation.
- Visualizations of score components.
- Personalized financial recommendations.

---

## Usage

1. **Launch the App**  
   Run the Streamlit app as described in the setup instructions.

2. **Input Data**  
   Enter your monthly income, savings, expenses, and debt in the input fields.

3. **View Results**  
   - The app displays your financial score.
   - Visualizations break down the components of the score.
   - Recommendations are provided to improve your score.

---

## Contributing

Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Example Visualization
To further enhance the README, you can include screenshots of the app interface or example outputs, if applicable.

