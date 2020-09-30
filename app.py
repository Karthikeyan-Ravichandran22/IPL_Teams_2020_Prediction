# Importing essential libraries
import streamlit as st
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first-innings-score-lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

st.title("The Indian Premier League (IPL) ")

st.write("IPL Preiction App")
temp_array = list()


st.sidebar.header("IPL Score Preiction App")
add_selectbox_batting=st.sidebar.selectbox("Select the Batting Team:",('Chennai Super Kings','Delhi Daredevils','Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))
add_selectbox_bowling=st.sidebar.selectbox("Select the Bowling Team:",('Chennai Super Kings','Delhi Daredevils','Kings XI Punjab','Kolkata Knight Riders','Mumbai Indians','Rajasthan Royals','Royal Challengers Bangalore','Sunrisers Hyderabad'))


if add_selectbox_batting == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
elif add_selectbox_batting == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
elif add_selectbox_batting == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
elif add_selectbox_batting == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
elif add_selectbox_batting == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
elif add_selectbox_batting == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
elif add_selectbox_batting == 'Royal Challengers Bangalore':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
elif add_selectbox_batting == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]       



if add_selectbox_bowling == 'Chennai Super Kings':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
elif add_selectbox_bowling == 'Delhi Daredevils':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
elif add_selectbox_bowling == 'Kings XI Punjab':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
elif add_selectbox_bowling == 'Kolkata Knight Riders':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
elif add_selectbox_bowling == 'Mumbai Indians':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
elif add_selectbox_bowling == 'Rajasthan Royals':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
elif add_selectbox_bowling == 'Royal Challengers Bangalore':
     temp_array = temp_array + [0,0,0,0,0,0,1,0]
elif add_selectbox_bowling == 'Sunrisers Hyderabad':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]




overs = st.sidebar.number_input('Overs:')
runs = st.sidebar.number_input('runs')
wickets = st.sidebar.number_input('wickets')
runs_in_prev_5 = st.sidebar.number_input('runs_in_prev_5')
wickets_in_prev_5 = st.sidebar.number_input('wickets_in_prev_5')

temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
data = np.array([temp_array])
my_prediction = int(regressor.predict(data)[0])



if st.sidebar.button('Click to Predict'):
    st.sidebar.write("The Predicted score",my_prediction)
    st.sidebar.success('This is a success message!')
    



audio_file = open(r"C:\Users\karth\Downloads\ayogi-309.mp3", 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')


video_file = open(r"C:\Users\karth\Downloads\CSK Ms Dhoni Vivo IPL 2020-(MirchiStatus.com).mp4", 'rb')
video_bytes = video_file.read()
st.video(video_bytes)



page_bg_img = '''
<style>
body {
background-image: url("https://wallpapercave.com/wp/wp2458584.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
