import streamlit as st
import pickle
import helper

# Load the model directly from the root directory
MODEL_PATH = "model.pkl"

# Load the model
model = pickle.load(open(MODEL_PATH, 'rb'))

# Streamlit app UI
st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
