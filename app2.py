### this is also same app with designed UI#######



import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- CUSTOM CSS (reduced shadows, simplified panels) ---
custom_css = """
<style>
@keyframes flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.85; }
}

.stApp {
    background-color: #00001a;
    color: #e6f7ff;
    font-family: 'Inter', sans-serif;
}

/* Simplified panel */
.glass-container {
    background: #0d1a33;
    border-radius: 12px;
    box-shadow: 0 0 8px rgba(0, 191, 255, 0.25);
    border: 1.5px solid #00bfff;
    padding: 20px;
    margin-bottom: 25px;
    transition: all 0.3s ease-in-out;
}
.glass-container:hover {
    box-shadow: 0 0 12px #ff4d4d;
    border: 1.5px solid #ff4d4d;
    transform: translateY(-2px);
}

/* Title */
h1 {
    color: #00bfff;
    text-align: center;
    text-shadow: 0 0 6px rgba(0, 191, 255, 0.7);
    animation: flicker 4s infinite alternate;
}

/* Subheaders */
h2, h3 {
    color: #ff4d4d;
    text-shadow: 1px 1px 2px #000;
}

/* Inputs */
.stSelectbox label, .stNumberInput label {
    color: #e6f7ff !important;
    font-weight: bold;
}
.stSelectbox div[data-baseweb="select"] > div:first-child, 
.stNumberInput input {
    background-color: #0d2840 !important;
    color: #f0f8ff !important;
    border: 1px solid #00bfff !important;
    border-radius: 6px;
}
[data-testid="stSelectbox"] svg {
    color: #ff4d4d !important;
}

/* Button */
.stButton>button {
    background-color: #ff4d4d;
    color: white; 
    font-weight: bold;
    border-radius: 6px;
    border: none;
    padding: 12px 30px;
    box-shadow: 0 3px 10px rgba(255, 77, 77, 0.4);
    transition: all 0.3s ease;
    text-transform: uppercase;
}
.stButton>button:hover {
    background-color: #00bfff;
    box-shadow: 0 3px 12px rgba(0, 191, 255, 0.5);
    transform: scale(1.02);
}

/* Result Cards */
.win-card-style, .loss-card-style {
    text-align: center;
    padding: 18px;
    border-radius: 12px;
    background-color: #0d2840;
}
.win-card-style {
    border: 2px solid #00bfff;
    box-shadow: 0 0 8px #00bfff;
}
.win-card-style h3 { color: #00bfff; margin-bottom: 5px; }
.win-card-style h1 {
    color: #e6f7ff;
    font-size: 3em;
    text-shadow: 0 0 6px rgba(0, 191, 255, 0.8);
}
.loss-card-style {
    border: 2px solid #ff4d4d;
    box-shadow: 0 0 8px #ff4d4d;
}
.loss-card-style h3 { color: #ff4d4d; margin-bottom: 5px; }
.loss-card-style h1 {
    color: #e6f7ff;
    font-size: 3em;
    text-shadow: 0 0 6px rgba(255, 77, 77, 0.8);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- DATA ---
teams = ['Sunrisers Hyderabad','Mumbai Indians','Royal Challengers Bangalore',
         'Kolkata Knight Riders','Kings XI Punjab','Chennai Super Kings',
         'Rajasthan Royals','Delhi Capitals']
cities = ['Hyderabad','Bangalore','Mumbai','Indore','Kolkata','Delhi',
          'Chandigarh','Jaipur','Chennai','Cape Town','Port Elizabeth',
          'Durban','Centurion','East London','Johannesburg','Kimberley',
          'Bloemfontein','Ahmedabad','Cuttack','Nagpur','Dharamsala',
          'Visakhapatnam','Pune','Raipur','Ranchi','Abu Dhabi',
          'Sharjah','Mohali','Bengaluru']

try:
    pipe = joblib.load("final.pkl")
except FileNotFoundError:
    st.error("Model file 'final.pkl' not found.")
    pipe = None

# --- UI ---
st.title('🏆 IPL Win Predictor')

st.markdown('<div class="glass-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    batting_team = st.selectbox('Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams))
with col3:
    toss_winner = st.selectbox('Toss Winner', [batting_team, bowling_team])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-container">', unsafe_allow_html=True)
col4, col5 = st.columns(2)
with col4:
    selected_city = st.selectbox('Host City', sorted(cities))
with col5:
    target = st.number_input('Target Score', min_value=0, value=180, step=1)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-container">', unsafe_allow_html=True)
col6, col7, col8 = st.columns(3)
with col6:
    score = st.number_input('Current Score', min_value=0, value=50, step=1)
with col7:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, value=6.0, step=0.1)
with col8:
    wickets = st.number_input('Wickets Lost', min_value=0, max_value=9, value=2, step=1)
st.markdown('</div>', unsafe_allow_html=True)

# --- PREDICTION ---
if st.button('🔮 Predict'):
    if pipe is None:
        st.error("Model not loaded.")
    elif batting_team == bowling_team:
        st.warning("Batting and Bowling teams cannot be the same.")
    else:
        runs_left = int(target - score)
        balls_left = int(120 - (overs * 6))
        current_wickets = int(10 - wickets)

        if balls_left <= 0:
            st.warning("Match has concluded (0 balls left).")
        else:
            crr = score / overs if overs > 0 else 0
            rrr = (runs_left * 6) / balls_left

            input_df = pd.DataFrame({
                'batting_team': [batting_team],
                'bowling_team': [bowling_team],
                'toss_winner': [toss_winner],
                'city': [selected_city],
                'runs_left': [runs_left],
                'balls_left': [balls_left],
                'wickets': [current_wickets],
                'target': [target],
                'crr': [crr],
                'rrr': [rrr]
            })

            result = pipe.predict_proba(input_df)
            loss_prob = result[0][0]
            win_prob = result[0][1]

            st.markdown('<div class="glass-container">', unsafe_allow_html=True)
            col_win, col_loss = st.columns(2)
            with col_win:
                st.markdown(f"""
                <div class="win-card-style">
                    <h3>{batting_team}</h3>
                    <h1>{round(win_prob * 100)}%</h1>
                </div>
                """, unsafe_allow_html=True)
            with col_loss:
                st.markdown(f"""
                <div class="loss-card-style">
                    <h3>{bowling_team}</h3>
                    <h1>{round(loss_prob * 100)}%</h1>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
