import streamlit as st 
import pandas as pd
import pickle

st.set_page_config(page_title='Home Prediction Prediction', page_icon='Home.jpg')
st.header('Welcome to Bengaluru Home Price Predictor')

df = pd.read_csv('copied.csv')
with open('RFModel.pkl','rb') as file:
    model = pickle.load(file)

with st.container(border=True):
    col1, col2 = st.columns(2)
    loc = col1.selectbox('Location', options=df['location'].unique())
    sqft = col2.number_input('Sq Ft', min_value=300)
    bath = col1.number_input('Bathrooms', min_value=1)
    bhk = col2.number_input('BHK', min_value=1)
    locations = list(df['location'].unique())
    locations.sort()
    input_values = [(locations.index(loc), sqft, bath, bhk)]
    c1,c2,c3 = st.columns([1.6,1.5,1])
    if c2.button('Predict Price'):
        out = model.predict(input_values)
        st.subheader(f'Total Price: {out[0]*100000}')