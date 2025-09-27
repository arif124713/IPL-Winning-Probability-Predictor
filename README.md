


# 🏏 IPL Winning Probability Predictor

A Streamlit-based machine learning web application that predicts the winning probability of an IPL match in real-time based on match parameters.


## 🚀 Features
- Select batting team, bowling team, and toss winner  
- Choose the host city  
- Input target score, current score, overs completed, and wickets lost  
- Live calculation of:
  - Runs left  
  - Balls left  
  - Current Run Rate (CRR)  
  - Required Run Rate (RRR)  
- Predicts win probability for both teams using a trained ML model  

---

## 🛠️ Tech Stack
- **Python**  
- **Streamlit** (Frontend + App)  
- **Pandas / NumPy** (Data handling)  
- **Scikit-learn / Joblib** (Model training & persistence)  

---

## 📂 Project Structure
```

IPL-Winning-Probability-Predictor/
│
├── final.pkl                # Trained ML model
├── app.py                   # Main Streamlit app
├── requirements.txt         # Dependencies
└── README.md                # Project documentation

````

---

## ▶️ Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/arif124713/IPL-Winning-Probability-Predictor.git
   cd IPL-Winning-Probability-Predictor


2. Create & activate virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 📊 Example Prediction

* **Batting Team**: CSK
* **Bowling Team**: MI
* **Target**: 180
* **Score**: 90/2 in 10 overs

👉 Output: Probability of CSK win = `65%`, MI win = `35%`

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).



