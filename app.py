import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
while(batting_team in teams):
    teams.remove(batting_team)
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target',min_value=0,step=1)

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score',min_value=0,step=1)
with col4:
    overs = st.number_input('Overs completed',min_value=0.00,max_value=20.00,step=0.01)
with col5:
    wickets = st.number_input('Wickets out',min_value=0,max_value=10,step=1)



if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
  
    crr = score/overs 
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
            background-image: url("https://wallpapercave.com/wp/wp7104495.jpg");
            
            background-position:center center;
            background-size:380px,750px;     
            background-repeat: no-repeat;
            background-attachment:scroll;  
               

            
         }}
         
         
         </style>
         """,
         unsafe_allow_html=True
     )

#add_bg_from_url() 

'''
Made by Shrutashraba
'''
