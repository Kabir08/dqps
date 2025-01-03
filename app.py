import streamlit as st
import pickle
import os
import requests
import helper

# Function to download the model file from Google Drive
def download_model(file_url, output_path):
    if not os.path.exists(output_path):
        st.text("Downloading model file...")
        response = requests.get(file_url, stream=True)
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        st.text("Download complete!")

# Link to the hosted model.pkl file on Google Drive
MODEL_URL = "https://drive.google.com/uc?export=download&id=1OWbj2U5wJKUzP6UEyC7HW_Ji-Gw7SXxj"
MODEL_PATH = "model.pkl"

# Download the model if not present
download_model(MODEL_URL, MODEL_PATH)

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
